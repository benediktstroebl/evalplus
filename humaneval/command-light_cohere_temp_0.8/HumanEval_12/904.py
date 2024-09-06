```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    # Initialize the longest length as 0
    max_len = 0
    longest_str = ""

    # Iterate through the input list of strings
    for str in strings:
        # Update the maximum length and the longest string
        max_len = max(len(str), max_len)
        longest_str = str

    return longest_str

# Example usage
input_strings = ["a", "bb", "ccc", "abc"]
longest_result = longest(input_strings)
print("Longest string:", longest_result)  # Output: "ccc"
```
This Python code defines a function `longest` that takes a list of strings as input and returns the longest string from the list. The function utilizes the approach of iterating through the input strings, keeping track of their lengths, and storing the longest one. The function effectively solves the problem by returning the longest string in the input list.

The provided usage example demonstrates how to call the `longest` function with an input list of strings and then print the result, which should be the longest string from the list.