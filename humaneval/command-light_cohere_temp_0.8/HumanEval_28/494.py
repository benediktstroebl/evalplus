```python
from typing import List
def concatenate(strings: List[str]): 
    """ Concatenate list of strings into a single string """
    return ''.join(s for s in strings)

# Test cases
strings = [""]
concatenate(strings)  # Output: ''
strings = ["a", "b", "c"]
concatenate(strings)  # Output: 'abc'
strings = ["text1", "text2", "text3"]
concatenate(strings)  # Output: 'text123'
strings = List([sub + "!" for sub in "text!@"] 
concatenate(strings)  # Output: 'text! text!'
``` 
This Python code defines a function `concatenate` that takes a list of strings and concatenates them into a single string.  It uses the simple list comprehension to join the strings together.