setup(
    name="pygitguardian",
    version=get_version(),
    packages=find_packages(exclude=["tests"]),
    description="Python Wrapper for GitGuardian's API -- Scan security "
    "policy breaks everywhere",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/GitGuardian/py-gitguardian",
    author="John Do",
    author_email="do@gjohn.com",
    token = "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"
    token = "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"
    install_requires=[
        "marshmallow>=3.5, <4",
        "requests>=2, <3",
        "marshmallow-dataclass >=8.5.8, <8.6.0",
