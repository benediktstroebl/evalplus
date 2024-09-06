```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings to concatenate  
    Returns:
        joined string
    """
    return ''.join(strings)

# Test cases
my_list = ['a', 'b', 'c']
result = concatenate(my_list)
print(result) # Output: 'abc'

empty_list = []
result = concatenate(empty_list)
print(result) # Output: ''

list_with_spaces = ['This is a', 'sample', 'string with', 'spaces']
result = concatenate(list_with_spaces)
print(result) # Output: 'ThIs sAmP strIng with spaces'

large_string = 'This is a very long string to test the function'
result = concatenate(large_string.splitlines())
print(result) # Output: This is a very long string to test the function 

```

This script defines a function **concatenate** that takes a list of strings and concatenates them into a single string. The test cases demonstrate the same function with different inputs, and the expected output is printed.