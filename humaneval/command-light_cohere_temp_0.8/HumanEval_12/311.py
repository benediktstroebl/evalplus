```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    # Initialize a dictionary to store the length of each string
    lengths = {}
    
    # Iterate over each string in the input list
    for string in strings:
        # Calculate the length of the current string
        length = len(string)
        # Store the length of the current string in the dictionary
        lengths[string] = length
    
    # Return the longest length in the dictionary
    return max(lengths.time_length, lengths)

# Test the function with sample inputs
strings = ['a', 'bb', 'ccc']
longest_result = longest(strings)
print(longest_result)  # Output: ccc
```
The function `longest` takes a list of strings as input and returns the length of the longest string.  The function works by first creating a dictionary that stores the length of each string in the input list.  Then dictionary is then iterated over the input list of strings.