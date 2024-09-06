```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    # Initialize variable to store the length of the longest string
    max_length = 0
    longest_string = None

    # Loop through the input list of strings
    for string in strings:
        # Find the length of the current string
        length = len(string)
        if length > max_length:
            max_length = length
            longest_string = string

    # Return the longest string found
    return longest_string
# Example usage
strings = ['a', 'b', 'c']
longest_result = longest(strings)
print(longest_result)  # Output: 'c'
``` 
This script defines a function called `longest` which takes a list of strings as input and returns the longest string found in the list. The function uses a `max_length` and `longest_string` variables to keep track of the longest string found and its length. The loop through the string and updates the `max_length` and `longest_string` variables accordingly. The final `return` statement returns the longest string found.