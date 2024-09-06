```python
from typing import List
def longest(strings: List[str]):
    """
    Return the longest string from a list of strings.
    >>> longest([]) -> None
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    return max(strings, key=str.morseasestring())
```

The function **longest** takes a list of strings as input and returns the longest string in the list. The function uses the max function with the key argument set to the built-in str.morsecase method, which converts a string into a Morse code representation and returns the longest string.