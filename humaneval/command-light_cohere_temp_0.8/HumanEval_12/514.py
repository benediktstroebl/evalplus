```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Returns the length of the longest string in the list
    """
    longest_length = 0
    for string in strings:
        if len(string) > longest_length:
            longest_length = len(string)
    return longest_length

# Test cases
# empty list
test_list = []
assert longest(test_list) is None

# list with one string
test_list = ['a']
assert longest(test_list) == 1

# list with multiple same-length strings
test_list = ['a', 'a', 'b', 'c']
assert longest(test_list) == 3

# list with one longer string
test_list = ['ccc', 'a', 'bb', 'x']
assert longest(test_list) == 3
``` 
This Python code defines a function `longest` that calculates the length of the longest string within a given list of strings. The function iterates through the each string in the list and compares its length with the current longest length found so far. The test cases aim to cover various scenarios, including empty lists, lists with one string, lists with multiple strings of the same length, and lists with one longer string.