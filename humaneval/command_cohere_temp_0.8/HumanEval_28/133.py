```python
# Import the necessary module
from typing import List

# Define the function
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    result = ''
    for string in strings:
        result += string
    return result

# Example usage
>>> concatenate([])
''
>>> concatenate(['a', 'b', 'c'])
'abc'
```

This code defines a function called `concatenate` that takes a list of strings as input and returns a single string as output. It then provides two example usages that demonstrate how the function works. 

In the first example, an empty list is passed in and the result is an empty string. In the second example, the list of strings ['a', 'b', 'c'] is passed in, and the result is the concatenated string 'abc'. 

This function is designed to concatenate all the strings in the list together and return the resulting single string.  It's useful when you need to join multiple strings together into a single string without any spaces or separators between them.  It does have a note that this is just a basic implementation, and if you need more advanced string concatenation with separators or formatting, further customization would be required.