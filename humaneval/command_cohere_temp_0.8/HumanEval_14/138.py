```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda s: s != '', string))));
```
The function `all_prefixes()` uses the `dropwhile()` function from the `itertools` module to iterate over the strings formed by dropping one character from the input string ( prefixes ). The `dropwhile()` function drops characters from the beginning of the string until a string is reached where the predicate returns false, which is achieved when the string is equal to an empty string. The iteration is reversed using the `reversed()` function to ensure the shortest prefixes are computed first and the result is a list of strings containing all the prefixes of the input string.  It is important to include the type `List[str]` in the function declaration so that the function returns the proper type in accordance with the typing library.