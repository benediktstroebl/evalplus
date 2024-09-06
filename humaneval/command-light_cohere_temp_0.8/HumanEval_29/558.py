```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    :param strings: List of strings
    :param prefix: String to filter for
    :return: List of strings with a given prefix
    """
    return [s for s in strings if s.startswith(prefix)]
```
Do you require assistance with another Python problem that can be solved using functional programming or with any other specific Python feature?