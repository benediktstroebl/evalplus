```python
from typing import List
def longest(strings: List[str]):
    # return the longest string from the list of strings
    return max(strings, key=len)

# Test case 1:
strings = ['a', 'b', 'c']
result = longest(strings)
assert result == 'a'  

# Test case 2:
strings = ['a', 'bb', 'ccc']
result = longest(strings)
assert result == 'ccc'  

# Test case 3:
strings = []
result = longest(strings)
assert result is None  

# Test case 4:
strings = ['a', 'bb', 'ccc', 'd']
result = longest(strings)
assert result == 'bb'
```
The function `longest` accepts a list of strings as input, and returns the length of the longest string in that list. It utilizes the max function with the `key=len` argument, which allows you to specify the key to compare based on length. The function will then return the first string in the list with the maximum length, or None if the list is empty.