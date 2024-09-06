```python
from typing import List
def concatenate(strings: List[str]): 
    """ Concatenate list of strings into a single string """
    return ''.join(s) for s in strings)

# Example usage:
strings = ['a', 'b', 'c']
print(concatenate(strings))  # Output: 'abc'
strings = []
print(concatenate(strings))  # Output: ''
``` 
This code defines a function called **concatenate** that takes a list of strings as input and returns a single string by concatenating the strings in the list. The function utilizes a list comprehension and the **join** method to achieve this.

The output for the example provided is 'abc' and an empty list, respectively.