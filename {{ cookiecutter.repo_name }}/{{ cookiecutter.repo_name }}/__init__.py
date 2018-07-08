import pkgutil 
import warnings

__path__ = pkgutil.extend_path(__path__, __name__)

imported = False
# find all subpackages and modules and import them
for importer, modname, ispkg in pkgutil.walk_packages(path=__path__, prefix=__name__+'.'):
    imported = True
    try:
        __import__(modname, globals(), locals())
    except ImportError:
        warning.warning('Failed to import '+__name__+'.'+modname)

# cleanup package namespace
del pkgutil, warnings
if imported:
    del importer, modname, ispkg
del imported
