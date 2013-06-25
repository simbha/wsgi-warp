import json
import mod_wsgi_installer

APACHE_CONFIG = """
ServerRoot /home/dotcloud
ErrorLog /home/dotcloud/logs/error_log
PidFile /home/dotcloud/logs/apache.pid

LoadModule authz_host_module /usr/lib/apache2/modules/mod_authz_host.so
LoadModule mime_module /usr/lib/apache2/modules/mod_mime.so
LoadModule rewrite_module /usr/lib/apache2/modules/mod_rewrite.so
#LoadModule wsgi_module /usr/lib/apache2/modules/mod_wsgi.so
LoadModule wsgi_module %(MOD_WSGI_MODULE_PATH)s

DefaultType text/plain
TypesConfig /etc/mime.types

MaxMemFree 64
ThreadStackSize 262144

ServerLimit 1
ThreadLimit 15
StartServers 1
MaxClients 15
MinSpareThreads 15
MaxSpareThreads 15
ThreadsPerChild 15
MaxRequestsPerChild 0

Listen %(PORT_WWW)s

DocumentRoot /home/dotcloud/current/htdocs

<Directory />
    Options FollowSymLinks
    AllowOverride None
    Order deny,allow
    Deny from all
</Directory>

<Directory /home/dotcloud/current/htdocs>
    Options ExecCGI
    AddHandler wsgi-script .wsgi
    Order allow,deny
    Allow from all
</Directory>
"""

if __name__ == '__main__':
    with open('/home/dotcloud/environment.json') as f:
        environ = json.load(f)

    environ['MOD_WSGI_MODULE_PATH'] = mod_wsgi_installer.module_location()

    print(APACHE_CONFIG % environ)
