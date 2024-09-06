```python
# Importing required module
from typing import List


# Defining function
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    concatenated = ''
    for string in strings:
        concatenated += string
    return concatenated
```

This function is designed to work with a list of strings and return a single string that is the concatenation of all the strings in the list. It begins with an empty string, and then adds the next string to it, creating a chain effect. 

The example usage and test cases provided earlier demonstrate how to use this function to solve the problem. 

Let me know if it addresses the problem you had in an accurate and concise manner. Feel free to ask if you have any more questions or if you'd like further clarification on any related topic.