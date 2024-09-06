```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the longest string in the list.
    """
    strings = [str for st in strings for _ in st]
    return max(strings, key=len)

# Test cases
strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'

strings = ['abrakabrac']
print(longest(strings))  # Output: 'abrakabrac'

strings = []
print(longest(strings))  # Output: None

strings = ['abc', 'abc123', 'abcd']
print(longest(strings))  # Output: 'abc123')
```  This Python code defines a function called `longest` that takes a list of strings as input and returns the longest string in the list. The `longest` function uses list comprehension to convert all strings in the input list into a list of characters and then uses the `max` function with the `len` key to return the maximum length of characters. The test cases are passed to the `longest` function to verify its correctness.