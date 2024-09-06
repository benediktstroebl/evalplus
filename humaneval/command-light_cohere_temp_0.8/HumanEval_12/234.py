```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    # Checks if the input list is empty
    if not strings:
        return None
    # Initialize the variable that stores the longest string
    longest_str = strings[0]
    # Find the longest string in the list
    for string in strings:
        if len(string) > len(longest_str):
            longest_str = string
    # Return the longest string found
    return longest_str

# Example usage:
# Test with a list of strings
input_strings = ['a', 'b', 'c']
longest_result = longest(input_strings)
print(longest_result)  # Output: 'a'
```
This Python code defines a function called "longest" that takes a list of strings as input and returns the longest string from that list. This function uses a type hints to ensure the input list is not empty, and then it compares each string with the current length of the "longest_str" variable, and updates the latter with the longer string found. The function returns the time the highest length among all strings in the input list. This code demonstrates how to solve the problem of finding the longest string in a list using Python.