```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda x: x != '', string))));
```
The function `all_prefixes()` uses the `dropwhile` function from the `itertools` module to iterate over the strings and exclude those that match the condition given by the lambda function `lambda x: x != ''`. The result is reversed to obtain the prefixes in ascending order and returned as a list.

This code incorporates type hints and docstrings to improve readability and maintainability, conforming to Python best practices.