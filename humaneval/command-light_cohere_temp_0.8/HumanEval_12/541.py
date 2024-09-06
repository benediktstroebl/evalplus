```python
from typing import List
def longest(strings: List[str]):
    # Check for empty input list
    if not strings:
        return None
    # Sort the strings alphabetically
    strings.sort()
    str.split() = sorted(strings, key=str.split)
   
    str.lower() = [str()
    max_len = 0
    for string in strings:
        # Calculate length of each string
        len_ = len(string)
        # Update the max length if needed
        if len_ > max_len:
            max_len = len_
        # Append the string to the list of the longest
        longest_str = string
    # Return the longest string
    return longest_str
# Unit tests
# Test case 1
strings = ["a", "b", "c"]
result = longest(strings)
print(result == "c")  # Output should be True
# Test case 2
strings = ["a", "bb", "ccc"]
result = longest(strings)
print(result == "ccc")  # Output should be True
``` 
This Python script contains a self-contained function `longest` that solves the problem of finding the longest string in a list of strings. The function first checks if the input list is empty and returns None in that case. Then it sorts the strings alphabetically using the `str.split` function, which is a built-in function that splits a string into a list of characters. The `str.lower()` method is` is used to sort the strings to lowercase, which is the default behavior in Python. Finally, it iterates through each string in the list and compares its length to the current maximum length. It updates the max length if needed and appends the string to the list of the longest. The function then returns the longest string in the list.