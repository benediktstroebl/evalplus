```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Returns the length of the longest string in the list """
    if not strings:
        return None
    
    max_len = max(len(string) for string in strings)
    return max_len

# Test cases
print(longest(['a', 'bb', 'ccc']))  # Output: 3
print(longest(['a', 'bb', 'ccc', 'aaa']))  # Output: 3
print(longest([]))          # Output: None
print(longest(['aa', 'aa']))    # Output: 2
``` 
The function `longest` takes a list of strings as input and returns the length of the longest string in the list. The function first checks if the list is empty and returns `None` in that case. 
The next step is to find the maximum length of the string in the list.