from setuptools import setup, find_packages


if __name__ == "__main__":
    setup(name ="virusTotal",
          description="Esta es una aplicacion hecha en python para usar virustotal",
          license="MIT",
          url="https://github.com/clr-csoc/virusTotal.git",
          version="0.0.1",
          author="Raul Villano Obregon",
          author_email="raulengineer@gmail.com",
          long_description=open('README.md').read(),
          packages=find_packages(),
          zip_safe=False,
          install_requires=["pandas","vt-py","openpyxl","numpy"],
        classifiers=[    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",]
          )