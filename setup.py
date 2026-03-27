from setuptools import setup, find_packages
from pathlib import Path

long_description = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")

setup(
    name="healome-clock",
    version="0.1.0",
    author="Nikhil Yadala",
    author_email="nikhil@healome.one",
    description="Open-source blood-based biological age estimation from standard clinical biomarkers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://healome.ai",
    project_urls={
        "Source": "https://github.com/nikhilYadala/healome_bio_age",
        "Bug Tracker": "https://github.com/nikhilYadala/healome_bio_age/issues",
        "Documentation": "https://github.com/nikhilYadala/healome_bio_age#readme",
    },
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21,<2",
        "pandas>=1.3",
        "scikit-learn>=1.0,<1.1",
        "joblib>=1.0",
        "matplotlib>=3.4",
        "huggingface_hub>=0.20",
    ],
    extras_require={
        "survival": [
            "lifelines>=0.27",
        ],
        "neural": [
            "torch>=1.9",
        ],
        "hub": [
            "huggingface_hub>=0.20",
        ],
        "dev": [
            "pytest>=7.0",
            "pytest-cov",
            "black",
            "ruff",
            "lifelines>=0.27",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],
    keywords="biological-age aging biomarkers blood-panel NHANES longevity",
)
