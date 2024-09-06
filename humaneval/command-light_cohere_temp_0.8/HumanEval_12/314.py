```python
from typing import List
def longest(strings: List[str]): 
    """
    Return the longest string from a list.
    >>> strings = ['a', 'b', 'b', 'a']
    return max(strings, key=len)
    """
#Tests
strings = ['a', 'bb', 'ccc']
print(longest(strings)) 
``` 
This code defines the longest function, which takes a list of strings as input and returns the longest string in the list. The function uses the max function with the key argument set to len to get the longest string. The test code section creates a list of strings ['a', 'bb', 'ccc'] and calls the longest function with this list, which should return 'ccc'.