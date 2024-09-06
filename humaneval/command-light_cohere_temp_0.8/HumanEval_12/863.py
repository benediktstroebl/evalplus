Here's the code:
```python
from typing import List
def longest(strings: List[str]):
    """ Outlines a function to return the longest string in a list of strings.
    return the max_length = max(len(x) for x in strings) )
    return max(strings)[len(strings[0])]

#Test the function
strings = ['a', 'b', 'c']
print(longest(strings)) 
# Expected Output: c

strings = ['a', 'bb', 'ccc']
print(longest(strings)) 
# Expected Output: c

strings = []
print(longest(strings)) 
# Expected Output: None

strings = ['a', 'bb', 'ccc']
print(longest(['aa', 'bb', 'ccc'])) 
# Expected Output: c
```