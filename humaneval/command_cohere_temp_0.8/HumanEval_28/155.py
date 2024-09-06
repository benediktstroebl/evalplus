```python
# Import the necessary module
from typing import List

# The function to concatenate the strings in the list
def concatenate(strings: List[str]) -> str:
    """
    Concatenate all strings in the list and return the result as a single string.
    """
    result = ''.join(strings)
    return result

# Example usage and test
strings = ['a', 'b', 'c']
print(f'Result: {concatenate(strings)}' )
# Output: Result: abc
```

This script includes the `concatenate` function, which takes a list of strings as input and uses the `join` method to concatenate them into a single string. Additionally, it provides an example usage and output to demonstrate the function's behavior.