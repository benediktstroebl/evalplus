Here is a Python script that contains a self-contained function that solves the problem of finding the longest string in a list of strings:
```python
from typing import List
def longest(strings: List[str]) -> str:
    # Initialize the variable to store the longest string
    longest_str = ""
    
    # Iterate through the list of strings
    for string in strings:
        # Compare the length of the current string with the previous length of the longest string
        if len(string) > len(longest_str):
            longest_str = string
    return longest_str
# Example usage
my_list = ['a', 'b', 'c']
print(longest(my_list))  # Output: 'c'
```
This script defines a function called `longest` that takes a list of strings as input and returns the longest string in the list. The function uses a variables to store the longest string encountered so far and loops through the list of strings. The function compares the string with the current length of the longest string found so far and updates the variable accordingly. 

This script can be used to find the longest string in any list of strings by passing the list to the `longest` function.