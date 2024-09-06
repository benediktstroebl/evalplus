```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate  
    Returns:
        str: Concatenated string
    """
    return ''.join(strings)

# Example usage:
strings = ['a', 'b', 'c']
print(concatenate(strings))  # Output: 'abc'
```
This Python code defines a function `concatenate` that takes a list of strings as input and concatenates them into a single string. It utilizes the string concatenation with the `join` function to combine the strings and then returns the concatenated result. The code also provides an simple example of using the `concatenate` function with a list of strings ['a', 'b', 'c'] and prints the result, which is the concatenated string 'abc'.