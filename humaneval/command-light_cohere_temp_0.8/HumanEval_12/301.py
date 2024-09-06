```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Return the longest string from a list of strings.
    Args: strings (List[str]): A list of strings
    Returns: Optional[str]: The longest string.
    """
    # Initialize variables
    longest = None
    max_length = 0
    for string in strings:
        # Check if the string is not empty
        if len(string) > 0:
            # Check if the current string is longer
            if len(string) > max_length:
                longest = string
                max_length = len(string)
    return longest
# Example usage
my_list = ['a', 'b', 'c']
print(longest(my_list))  # Output: 'a'
my_list = ['a', 'bb', 'ccc']
print(longest(my_list))  # Output: 'ccc'
 ```
This function, named longest, takes a list of strings as input and returns the longest string found in the list. It initializes two longest and max_length variables, and a loop iterates through the input strings. It compares each string against the