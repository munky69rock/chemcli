from setuptools import setup
import chemcli

setup(
        name="chemcli",
        version=chemcli.__version__,
        author="AIDD",
        author_email="aidd-dls_my@dena.jp",
        description="cli tools for chemoinfomatics with less dependencies",
        license="MIT",
        install_requires=[],
        tests_require=[
            "nose",
            "flake8",
            "flake8-import-order",
            ],
        packages=["chemcli"],
        scripts=["scripts/sdf"]
        )
