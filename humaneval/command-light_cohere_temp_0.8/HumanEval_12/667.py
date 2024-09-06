```python
from typing import List
def longest(strings: List[str]): 
    """ Returns the longest string in the list
    """
    return max(strings, key=len)

# Test case
test_strings = ["a", "bb", "ccc"]
longest(test_strings) # Output: 'ccc'
```
The code defines a function called "longest" that takes a list of strings as input. The function uses the maximum function to find the longest string in the list, using the 'max' function and the 'len' function to get the length of each string.

It returns the longest string as the output. 

The code also includes a test case that passes the test.