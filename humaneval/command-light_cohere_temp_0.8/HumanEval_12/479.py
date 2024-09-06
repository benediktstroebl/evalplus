```python
from typing import List
def longest(strings: List[str]):
    # Validate input
    if not strings:
        return None

    # Initialize variables
    max_length = 0
    longest_string = ""

    # Loop through strings and find the longest
    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
            longest_string = string

    return longest_string

# Unit tests:
- Test with an empty list
result = longest([])
assert result is None

- Test with a list of strings of different lengths
result = longest(['a', 'bb', 'ccc'])
assert result == 'ccc'
```
The provided code defines a function `longest` that takes a list of strings as input and returns the longest string from the list. It uses a validation to check if the input list is empty, in which case it returns `None`. It also uses a loop to iterate through the strings and find the longest one by comparing its length to the current maximum length. The code includes unit tests to ensure the functionality is correctly implemented.