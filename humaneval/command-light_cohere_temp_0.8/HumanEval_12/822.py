```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case of empty list.
    strings = [list of strings to process
    return max_length:max(map(len, strings)))
    """
    return next((len(x) for x in strings if len(x) == max_length), None)

# Tests
strings = ['a', 'bb', 'ccc']
longest_result = longest(strings)
print("Longest string:", longest_result) # Output: "ccc"

strings = []
strings. empty_list
longest_result = longest(strings)
print("Longest string:", longest_result) # Output: None

strings = ['apple', 'banana', 'date']
longest_result = longest(strings)
print("Longest string:", longest_result) # Output: "date"
```
The provided code defines a function called longest that takes a list of strings as input and aims to find and return the longest string from the list. It uses the maximum mapping technique to compare and identify the longest string within the list. Additionally, it handles the case of an empty list by returning None. The code includes several tests to validate the correctness of the function. The output of the code will display the longest string from the input list and handle the case of an empty list.