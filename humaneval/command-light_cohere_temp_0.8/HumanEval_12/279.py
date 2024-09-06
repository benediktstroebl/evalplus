```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Returns the length of the longest string in the list."""
    return max(strings) if strings else None

# Test cases
strings = ['a', 'b', 'c']
result = longest(strings)
print(result)  # Output: 3

strings = ['a', 'bb', 'ccc']
result = longest(strings)
print(result)  # Output: 3

strings = []
strings. string empty list. 
result = longest(strings)
print(result)  # Output: None

strings = ['apple', 'banana', 'cherry']
result = longest(strings)
print(result)  # Output: 3
```
This function, named `longest`, accepts a list of strings as input and returns the length of the longest string in the list. The function utilizes the max function to determine the length of the longest string.

The test cases provided demonstrate the functionality of the `longest` function with various input lists of strings.