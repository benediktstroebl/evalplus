```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings to concatenate  
    Returns:
        str: concatenated string
    """
    return ''.join(strings)
```

This script defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. The `concatenate` function uses the `join` method to combine the strings into a single string, ensuring a clean and readable code.