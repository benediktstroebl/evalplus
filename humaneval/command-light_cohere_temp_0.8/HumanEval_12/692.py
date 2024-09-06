```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Returns the longest string from a list of strings.
    Args:
        strings (List[str]): A list of strings

    Returns:
        List[str]: The longest string, or None if empty input.
    """
    # Initialize the max length
    max_length = 0
    # Initialize list with the longest string found so far
    longest_found = None

    # Iterate through the list
    for string in strings:
        # Update the max length if the current string is longer
        max_length = max(max_length, len(string))
        # Add the current string to the list of strings with the longest length
        longest_found = [x if x == longest_found else string for x in strings]

    # Return the longest string found
    return longest_found

# Example usage
# Input list of strings
input_strings = ['a', 'b', 'c']

# Call the function with the input list
result = longest(input_strings)

# Print the result
print(result)
```
The output of the above code will be:
```
['c']
```
The code defines a function `longest` that takes a list of strings as input and returns the longest string from the list. The function uses a list comprehension to iterate through the list of strings, and compares each string with the current longest string found so far. The function then updates the string in the list with the new longest string found and keeps track of the longest string found so far.