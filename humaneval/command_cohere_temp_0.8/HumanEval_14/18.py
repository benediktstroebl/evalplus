```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda x: x == string[0:len(x)], string[1:]+string))))
```

The `dropwhile` function is used to iterate over the substrings of the input `string` with the help of the `itertools` module. The `dropwhile` function drops the substrings which are equal to the preceding substring and iterates over the remaining. The list of returned substrings is then reversed to ensure that the shortest prefix comes first and the longest one is at the end.

The implementation is concise and efficient but it is not self-explanatory. To make it easier to understand, a verbose explanation could be added in the docstring like this:
```python
from typing import List
from itertools import dropwhile

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string 
    It does this by iterating over the substrings of the input string using the dropwhile function from the itertools module. 
    This function drops the substrings equal to the preceding substring and iterates over the remaining. 
    The list of remaining substrings is reversed to ensure the order from shortest to longest. 
```

This adds a more detailed explanation of the implementation and how the `dropwhile` function is used to achieve the desired result.