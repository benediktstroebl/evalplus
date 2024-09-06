```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda x: x == string[0:len(x)], string[1:]+string))))
```

The `dropwhile` function is used to generate an iterator excluding strings that are equal to prefixes of the full string and recursively capturing these prefixes. The resulting iterator is reversed to retrieve the correct order and converted into a list. 

Would you like to know more about any of the functions used in the code?