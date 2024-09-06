Here is a self-contained Python script that solves the problem of joining a list of strings into a single markdown code block:
```python
from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string using markdown code
    :param strings: List of strings to concatenate
    :return: Concatenated string in markdown format
    """
    return "\n".join(strings)
```