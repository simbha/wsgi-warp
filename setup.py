from setuptools import setup

setup(name = 'warpdrive',
      version = '0.9',
      description = 'Launcher for SGI applications.',
      author = 'Graham Dumpleton',
      author_email = 'Graham.Dumpleton@gmail.com',
      license = 'BSD',
      url = 'https://github.com/GrahamDumpleton/wsgi-warp',
      packages = ['warpdrive', 'warpdrive.dotcloud'],
      scripts = ['warp-admin'],
     )
