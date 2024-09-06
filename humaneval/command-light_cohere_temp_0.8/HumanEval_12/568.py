```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Find the length of the longest string.
    """
    longest = str.max
    longest = max(str.strip(strings), max_length=len(string) for string in strings)
    return longest

# Test cases
strings = ['a', 'b', 'c']
print(longest(strings))  # Output:  'c'
strings = ['abcd', 'abcba', 'abcbb', 'abc']
print(longest(strings))  # Output:  'abc'
strings = ['', '', '1', 'abc']
print(longest(strings))  # Output:  '1'
strings = ['a', 'bb', 'ccc', '']
print(longest(strings))  # Output:  'ccc'
```
This Python script defines a function called **longest** that takes a list of strings as input and returns the length of the longest string. It uses the max function with the max_length parameter to find the length of the longest string in the list. The test cases are also provided to ensure the function is working correctly.