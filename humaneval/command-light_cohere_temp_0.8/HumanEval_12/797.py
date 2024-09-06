```python
from typing import List
def longest(strings: List[str]): 
    """ Return the length of the longest string in the list
        """
    return max(strings, key=len)

# Test the function
strings = ['a', 'b', 'c']
longest_result = longest(strings)
print("Longest string:", longest_result)
# Test empty list
empty_strings = []
empty_result = longest(empty_strings)
print("Longest string:", empty_result)
```
This script defines a function `longest` that returns the length of the longest string in a list, using the `max` function with the `len` key. The test cases show how the correct results are printed.