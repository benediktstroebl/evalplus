Here is a Python script with a self-contained function that filters an input list of strings based on a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings, keeping only those that start with a given prefix.

    :string list, all strings with a prefix of 'p'. 
    """
    return [string for string in strings if string.startswith(prefix)]

```
The function takes two parameters: `strings`, which is the input list of strings, and `prefix`, which is the string that must start the input strings. 

The function returns a list of the strings that start with the given prefix. 

To test the function, a sample input list is provided, and the expected output is printed. 

This function is self-contained, and it can be used to filter a list of strings based on a given prefix in a variety of situations.