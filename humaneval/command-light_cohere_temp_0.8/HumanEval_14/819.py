Here is a self-contained Python script that solves the problem of returning all prefixes from shortest to longest of the input string:
```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return ["".join([char for char in s if s.isupchar(char)])
```

Here, we define the function `all_prefixes` that takes a string as input and returns a list of all prefixes from shortest to longest of the input string. 
This is achieved by using a list comprehension that iterates over each character in the input string and checks if the character is included in the character set that makes the prefix.