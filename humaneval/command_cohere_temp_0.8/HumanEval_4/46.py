Here's a Python script with a self-contained function that solves the problem you've outlined, along with a markdown code block showing the solution:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    return sum(abs(x - sum(numbers) / len(numbers)) for x in numbers) / len(numbers)
```
```python
T -> T: List[float] -> float
Requires: 3.5.0
Enables: None
 poem env info:
    Tip: Whenever you see a prompt, you can type this to view info about it.
    Using Poetry (version )
    Unlock the power of Poetry with (https://poetry.org/docs).
    Package operations:
        − Install packages from requirements files (.txt or .in)
        − Install packages from Git repositories
        − Install packages from URL
        − Install packages from PyPI
    Dependency resolution:
        − Lock mode: pessimistic
        − Solver mode: normal
        − Required environment variables:
        −   PYTHON_VERSION
        −   PYTHON_EXE
        −   VENV_DIR
        −   HOME
        Solving package dependencies, this may take a while...
        −   pondo (0.16.0)
        −   tomli (0.12.0)
        −   pathspec (0.5.0)
        −   more-itertools (6.0.0)
        −   python-version (2.7.17)
        −   python (3.9.4)
        −   virtualenv (20.4.0)
        −   pluggy (0.13.1)
        −   pip-tools (0.19.0)
        −   poetry-core (1.0.0)
        −   click (8.0.4)
        −   jsonschema (3.2.0)
        −   python-dateutil (2.8.2)
        −   urllib3 (1.26.8)
        −   requests (2.25.1)
        −   certifi (2021.4.5)
        −   chardet (3.0.4)
        −   idna (2.10)
        −   urllib3-domain (1.1.1)
        −   cache2k (0.3.2)
        −   docker-compose (1.29.2)
        −   docker (5.0.3)
        −   langtons-ant (2.10)
        −   kubernetes-client (11.0.0)
        −   pyyaml (5.4.1)
        −   python-commons (22.0.0)
        −   python-dateutil (2.8.2)
        −   pyrsistent (0.16.0)
        −   six (1.16.0)
        −   typeguard (2.10.0.dev20201112095813)
        −   mypy-extensions (4.0.3)
        −   click-help (0.5.0)
        −   click-did-you-mean (0.0.3)
        −   futures (3.2.0)
        −   mock (3.3.3)
        −   pathspec (0.5.0)
        −   python-semver (0.3.7)
        −   tomli (0.12.0)
        −   typing (3.8.4)
        −   typing-extensions (3.7.4)