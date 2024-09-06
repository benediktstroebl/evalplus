```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda x: x != '', string))));
```
The function `all_prefixes()` uses the `dropwhile` function from the `itertools` module to iterate over the strings, dropping those that are not the prefix of another string (i.e., dropping the prefixes themselves). The resulting list of strings is then reversed to ensure that the shortest prefixes are listed first, and returned. 
The code includes type annotations, adding additional information to the function to indicate that the function takes a string parameter and returns a list of strings. These type annotations can be used by an IDE or other programming tools to provide more accurate code completion and checking.
This code assumes that the input string is non-empty. If this assumption is not met, the function will throw an error. If the input string is empty, the function will return an empty list.