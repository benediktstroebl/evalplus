Here is a self-contained Python script that defines a function `all_prefixes`, which returns a list of all prefixes from shortest to longest of the input string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return list( divisors(string) for i,div in enumerate(string.split()) )
```

This script defines a function that takes a string as input and returns a list of all prefixes in the string. The function uses the string.s worst-case approach to get the prefixes by iterating through the string's character indexes and using the `split()` function to split the string into individual characters. The loop then iterates over the character indexes and creates a list of divisors of each character.