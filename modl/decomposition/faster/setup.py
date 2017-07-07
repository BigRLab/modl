from distutils.extension import Extension

import numpy
from Cython.Build import cythonize


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration('faster', parent_package, top_path)

    extensions = [
        Extension('modl.decomposition.faster.dict_fact_fast',
                  sources=['modl/decomposition/faster/dict_fact_fast.pyx'],
                  include_dirs=[numpy.get_include(),
                                'modl/decomposition/faster/_utils'
                                '/randomkit'],
                  ),
    ]
    config.ext_modules += extensions

    config.add_subpackage('_utils')

    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup

    setup(**configuration(top_path='').todict())
