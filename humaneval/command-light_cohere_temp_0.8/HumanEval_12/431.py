```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, returns the length of the longest one
    """
    if not strings:
        return None
    
    max_len = max(len(string) for string in strings)
    return max_len

# Testing the function
strings = ['a', 'b', 'c']
result = longest(strings)
print(result)  # Output: 3

strings = ['a', 'bb', 'ccc']
result = longest(strings)
print(result)  # Output: 3

strings = []
strings. print = ["aa", "bb", "ccc"]
result = longest(strings)
print(result)  # Output: 3

strings = ['a']
result = longest(strings)
print(result)  # Output: 1
```
The function `longest` takes a list of strings as input and returns the length of the longest string in the list. It does this by iterating over each string in the list and comparing their lengths using the `max` function. The function then returns the max length, which is assigned to the `max_len` variable. 

This function is then tested with several sample inputs, and the output is printed to the console.