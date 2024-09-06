```python
from typing import List
def longest(strings: List[str]):
    # function to find the longest string
    max_length = 0
    longest_str = ""
    for str in strings:
        # Check if the length of the string is greater than the current maximum length
        if len(str) > max_length:
            max_length = len(str)
            longest_str = str

    # If the list of strings is empty, return None
    return longest_str if longest_str else None
# Testing the function
test_strings = ["a", "bb", "ccc"]
result = longest(test_strings)
if result is not None:
    print("Longest string:", result)
else:
    print("No strings in the list.")
```
The provided code defines a Python script with a self-contained function `longest`, designed to find the longest string from a list of strings. The function utilizes a list of strings as its input and iterates through each string in the list. The function then calculates the string with the longest length, storing it in the variable `longest_str`. The function also updates the `max_length` variable. 

The test section follows, where a list of strings `test_strings` is used to call the `longest` function. The result variable is then assigned to the result of the function call. The test strings list is defined using a list of strings, and it is passed to the `longest` function to find the longest string. The script then checks if the result is not None, and prints the `longest_str` variable, representing the longest string in the list, else it prints a message indicating that the list is empty.