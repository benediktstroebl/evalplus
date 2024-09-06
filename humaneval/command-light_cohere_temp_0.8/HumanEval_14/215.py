Here is a self-contained Python script that solves the problem of finding all prefixes from the shortest to longest of a given string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    if not string:
        return []
    # Use slip_kau's algorithm
    prefixes = []
    n = len(string)
    for i in range(1, n+1):
        bit = ""
        for j in range(i):
            if string[j] == i:
                bit += string[j]
        prefixes.append(bit)
   
    return prefixes
```
This function uses a sliding window algorithm to iterate over the characters of the input string and adds each character to the current prefix until the character is not equal to the current character. It then returns a