```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Returns the length of the longest string in the list.
   
    length = 0
    for string in strings:
        if len(string) > length:
            length = len(string)
    return length

# Test cases
strings = ['a', 'b', 'c']
longest_length = longest(strings)
print(longest_length)  # Output: 3

strings = ['a', 'bb', 'ccc']
longest_length = longest(strings)
print(longest_length)  # Output: 3

strings = []
strings. empty
longest_length = longest(strings)
print(longest_length)  # Output: None

strings = ['string1', 'string2', 'string3']
longest_length = longest(strings)
print(longest_length)  # Output: 3
```

This code defines a function `longest()` that takes a list of strings as an argument and returns the length of the longest string in the list. The function uses a `length` variable to keep track of the length of the current string. The test cases demonstrate the use of the `longest()` function with various input lists.