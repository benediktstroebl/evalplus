```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Return the length of the longest string in the list.
    """
    # Initialize the max length to 0
    max_length = 0
    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
    return max_length

# Test cases
# Test empty list
test_empty = [()]
assert longest(test_empty) == None

# Test single string
test_single = ['a']
assert longest(test_single) == 1

# Test list of strings
test_list = ['a', 'bb', 'ccc']
assert longest(test_list) == 3

# Test list of same length strings
test_list_same = ['a', 'a', 'a', 'a']
assert longest(test_list_same) == 4
```
The `longest` function takes a list of strings as input and returns the length of the longest string in the list. This is to ensure that the input is a list of strings, the function uses a `for` loop to iterate over the list and find the longest string. The maximum length is stored in the `max_length` variable and returned as the output. 
To test the function, the test cases use the `assert` statement to verify that the function works correctly for different inputs.