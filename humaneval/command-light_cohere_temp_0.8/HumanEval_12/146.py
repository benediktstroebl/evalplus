Here is a Python script with a self-contained function that solves the problem of finding the longest string in a list of strings:
```python
from typing import List
def longest(strings: List[str]) -> str:
    # Taking the list of strings
    if not strings:
        return None
    # Using Python's built-in function to sort the list
    strings.sort(str)
    # Taking the list of sorted strings
    longest_str = strings[0]
    # Go through each string in the list and update the longest one
    for string in strings[1:]:
        if len(string) > len(longest_str):
            longest_str = string
    return longest_str

# Testing the function
test_strings = ['a', 'b', 'c']
longest_test = longest(test_strings)
print("Longest string from list:", longest_test)
```
The code defines a function called `longest` that takes a list of strings as input. The function first checks if the list is empty and returns `None` in that case. Then, it sorts the list of strings and assigns the first string in the sorted list as the `longest_str`. After that, it compares the length of the `longest_str` and all other strings in the list and updates `longest_str` with the longer one. This process continues until all longest string in the list is found.