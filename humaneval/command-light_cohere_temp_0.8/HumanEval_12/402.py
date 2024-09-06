```python
from typing import List
def longest(strings: List[str]) -> str:
    """ Return the length of the longest string in the list """
    max_length = 0
    longest_str = ""

    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
            longest_str = string

    return longest_str

# Example usage
strings = ["a", "b", "c"]
print(longest(strings))  # Output: "ccc"
``` 
This code defines a function `longest` that takes a list of strings and returns the length of the longest string. 
It iterates over the strings and calculates the length of each, comparing it to the current maximum length. The longest string is then stored in the variable `longest_str`, and the function returns this value.