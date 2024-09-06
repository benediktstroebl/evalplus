```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.
    """
    test_ longest([]) == None:
        raise ValueError("Input list is empty")
    
    if not strings or len(strings) == 0:
        return None
    
    return max(strings, key=len)

# Example usage
result = longest(['a', 'bb', 'ccc'])
print(result)  # Output: 'ccc'
``` 
This code defines a function `longest` that takes a list of strings as input and returns the longest string. It then performs several checks to ensure that the input list is not empty and contains at least one string. 

Finally, it returns the longest string in the list using the `max` function with the `key=len` argument, which ensures that the longest string is returned.