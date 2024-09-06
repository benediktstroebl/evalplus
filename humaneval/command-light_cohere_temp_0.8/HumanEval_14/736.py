```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join.[i for i, c in string if c != ' ' and c.value > 0]

    """ Validate input string
    > string = input("Enter a string: ")
    assert isinstance(string, str)

    """ Check if the string has a length greater than 0
    """
    assert len(string) > 0

    """ Extract all prefixes from shortest to longest
    """
    prefixes = ["".join.[i for i, c in string if c != " " and c.value > 0]

    return prefixes
```

You can use this function to get all prefixes of a given string.