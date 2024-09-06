Here's a self-contained Python script that defines a function to solve the problem of finding the longest string in a list of strings:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Return the longest string in the list.
    Parameters:
    strings (List[str]): List of strings

    Returns:
    str: The longest string
    """
    if not strings:
        return None
    return max(strings, key=len)

# Example usage
my_list = ['a', 'b', 'c']
print(longest(my_list))  # Output: 'a'

my_list = ['a', 'bb', 'ccc']
print(longest(my_list))  # Output: 'ccc'

my_list = []
my_list.add('The longest sentence')
print(longest(my_list))  # Output: 'The longest sentence'
```
The function longest takes a list of strings as input and returns the longest string in the list. The function first checks if the input list is empty, and if so, returns None. If the list is not empty, the function uses the `max` function with the `len` key argument to find the maximum length of the string in the list, and returns that string.