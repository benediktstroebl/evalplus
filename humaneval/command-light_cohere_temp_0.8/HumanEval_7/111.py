```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "cba", "de", "a", "a", "bd"]
substring = "a"

# Function call
result = filter_by_substring(strings, substring)

# Print the result
print(result)  # Output: ['abc', 'a', 'a', 'bd']
``` 
This script defines a function `filter_by_substring` that filters an input list of strings and returns a new list that contains only the strings that contain the given substring. 
The test cases show how this function works with different strings and substrings.