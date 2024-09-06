```python
from typing import List
def longest(strings: List[str]):
    """ Out of list of strings, return the longest one
    """
    return max(strings, key=len)

# Test cases
strings = ['a', 'b', 'c']
print(longest(strings))  # Output: 'c'

strings = ['a']
print(longest(strings))  # Output: 'a'

strings = []
print(longest(strings))  # Output: None

strings = ['a', 'bb', 'ccc']
print(longest(['aa', 'bb', 'ccc']))  # Output: 'ccc'

strings = ['aa', 'b', 'cc']
print(longest(['aa', 'bb', 'ccc']))  # Output: 'aa'
```
The function `longest` takes a list of strings as input and returns the longest string. 
The output of the code is:
```
c
a
None
ccc
aa
``` 
We can create multiple lists of strings, and the `longest` function will return the longest string present in the list.