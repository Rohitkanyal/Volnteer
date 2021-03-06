from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(
        "solr_builder/solr_builder.py", compiler_directives={'language_level': "3"}
    )
)
