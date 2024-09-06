```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one, or None.
    """
    strings = [str for str in strings if str]
    if not strings:
        return None
    return max(strings, key=len)

# Test cases
print(longest(['a', 'b', 'c']))  # Output: 'a'
print(longest(['a', 'bb', 'ccc'])))  # Output: 'ccc'
print(longest([]))        # Output: None
print(longest(['aa', 'b', 'ccc']))  # Output: 'ccc'
``` 
The function `longest` takes a list of strings and returns the longest one, or `None` if the list is empty. The key argument is used to sort the list based on the length of each string. 

Please note that you can use this function in your markdown code block, or you can copy and paste it into your Python environment and run it.