```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    
    # Initialize an empty string
    result = ""
    
    # Add each string to the result
    for string in strings:
        result += string

    return result

# Example usage
my_list = ["a", "b", "c"]
print(concatenate(my_list))  
``` 
This code defines a function `concatenate` that takes a list of strings as input and returns a concatenated string. It uses a the string concatenation process within the function, passing in a sample list of strings to test its correctness. The output of the code will be a single string 'abc', as expected.