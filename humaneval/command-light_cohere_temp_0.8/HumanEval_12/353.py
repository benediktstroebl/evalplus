```python
from typing import List
def longest(strings: List[str]) -> str:
    # Validate input parameters
    if not strings:
        raise ValueError("Input list cannot be empty.")

    # Initialize variables
    max_length = 0
    current_length = 0
    longest_string = ""

    # Iterate through the list of strings
    for string in strings:
        if len(string) > current_length:
            current_length = len(string)
        longest_string = string

    return longest_string
```
The function `longest` takes a list of strings as input and returns the longest string from the list. It also includes input validation to ensure the input is not empty. The function iterates through each string in the list to find the longest one.