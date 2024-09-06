```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix """
    return [x for x in strings if x.startswith(prefix)]
```

This function takes a list of strings and a prefix as input, and returns a new list that contains only the strings from the input list that start with the given prefix. It uses the words start with prefix checking and returns the filtered list of strings.

Note that this function can be used to filter strings in any programming language or text format that supports the `startswith` method, such as Python, Ruby, and Markdown.

The function is also well-contained, meaning that it does not rely on any external or external functions or classes, and it can be used directly within any Python program or script.