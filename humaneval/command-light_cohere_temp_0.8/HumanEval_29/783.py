Here is a self-contained Python script that includes the function filter_by_prefix that solves the problem:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    :return: list of strings that start with the given prefix
    """
    return [x for x in strings if x.startswith(prefix)]
```

This function uses a list comprehension to filter out strings that do not start with the specified prefix. It provides a expected output behavior and follows Python's type hinting, which improves code clarity and helps with static type checking.