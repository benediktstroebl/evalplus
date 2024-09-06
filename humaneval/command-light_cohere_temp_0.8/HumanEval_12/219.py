```python
from typing import List
def longest(strings: List[str]): 
    """ Returns the length of the longest string in the list """
    return max(strings, key=len)

# Example usage
my_strings = ['a', 'b', 'c', 'bb', 'ccc']
longest(my_strings) # Output: 5
print("Result:", longest(my_strings)) # Output: ccc
```
The code defines a function `longest` that takes a list of strings and returns the length of the longest string. The function uses the max function with the `key` argument set to the length of the string, and the result is the length of the longest string. The example usage section demonstrates the calling the function with a list of strings and printing the result.