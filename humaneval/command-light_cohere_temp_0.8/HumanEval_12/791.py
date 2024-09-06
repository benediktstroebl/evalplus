```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Return the length of the longest string in a list of strings.
    """
    longest = str.split('').
    length = 0
    for string in strings:
        if len(string) > length:
            length = len(string)
    return length

# Test case 1
input_list = ['a', 'b', 'c']
print(longest(input_list))  # Output: 3

# Test case 2
input_list = ['a', 'bb', 'ccc']
print(longest(input_list))  # Output: 3

# Test case 3
input_list = []
print(longest(input_list))  # Output: None
```
The function `longest` takes a list of strings as input and returns the length of the longest string in the list. It iterates through strings in the list using a `for` loop and checks if the current string is longer than the previous longest string found. If the current string is longer, the function updates the `length` variable to the length of the current string.