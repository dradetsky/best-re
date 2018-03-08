try:
    import re2 as re
except (ImportError, ModuleNotFoundError):
    import re

def copy_module_here(mod):
    for key in dir(mod):
        globals()[key] = getattr(mod, key)

copy_module_here(re)
