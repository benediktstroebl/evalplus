```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    
    Returns:
        str: Concatenated string
    """
    return "".join("".join(strings)  )

# Test
my_list = ["a", "bc", "de"]
result = concatenate(my_list)
print(result) # Output: abcde 
```