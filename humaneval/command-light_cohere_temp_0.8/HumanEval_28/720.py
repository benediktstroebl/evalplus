```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings to concatenate
    Returns:
        string
    """
    return ''.join(strings)

# tests
print(concatenate([]))  
print(concatenate(['a']))   
print(concatenate(['a', 'bcde']))  
print(concatenate(['a','bcde', '!ed']))
``` 
This code defines a function called **concatenate** that takes a list of strings as an argument and concatenates them into a single string, returning that string.

The function uses the **join()** method to concatenate the list of strings.

Then the code prints the result of the function for different inputs and ensures the expected output is correctly generated.