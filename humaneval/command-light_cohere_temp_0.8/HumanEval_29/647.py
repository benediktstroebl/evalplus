Here's a self-contained Python script with a function that filters an input list of strings based on a given prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    : Return a Strings must all be lowercase to match the prefix.

    If matches all strings with the given prefix, return them as a new list.
    """
    common prefix, lowercase
    return_list = [s for s in strings if s.startswith(prefix.lower())]

    return return_list
    ```
```
The above function takes a list of strings and a prefix as input and returns a new list that contains only the strings from the input list that start with the specified prefix.