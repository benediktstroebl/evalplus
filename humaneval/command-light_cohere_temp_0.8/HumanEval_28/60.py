```python
from typing import List
def concatenate(strings: List[str]): 
    """ Function to concatenate list of strings into a single string """
    result = ''.join(''.join(strings)  # use join to convert list to a single string
    return result
# Test case 1: empty list
print(concatenate([])) 
# Expected output: ''

# Test case 2: single string
print(concatenate('a')) 
# Expected output: 'a'

# Test case 3: list of strings
print(concatenate(['a', 'b', 'c'])) 
# Expected output: 'abc'
```  This script defines a function `concatenate` that takes in a list of strings and returns a concatenated string. The function uses the specific type hints for the input parameter, which is a list of strings. The function then uses the join method to concatenate all the strings in the list into a single string.