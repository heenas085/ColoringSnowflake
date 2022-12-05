import setuptools
setuptools.setup(
     name='coloringsnowflake',
     version='0.1',
     scripts=['let_it_snow'] ,
     url="https://github.com/heenas085/ColoringSnowflake",
description='snowflake package to color the flakes',
      author='Heena Shaikh',
      author_email="heenas085@gmail.com",
install_requires= ['random', 'numpy', 'turtle'],
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )