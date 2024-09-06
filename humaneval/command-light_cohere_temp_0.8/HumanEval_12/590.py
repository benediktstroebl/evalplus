```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    # Initialize a variable to store the length of the longest string
    max_length = 0
    longest_str = ""

    # Iterate through the list of strings
    for string in strings:
        # Find the length of the current string and update the maximum length
        length = len(string)
        if length > max_length:
            max_length = length
            longest_str = string

    # Return the longest string found
    return longest_str
#example usage
my_list = ['a', 'b', 'c']
result = longest(my_list)
print(result)  # Output: 'c'
```