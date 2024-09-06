```python
from typing import List
def longest(strings: List[str]) -> str:
    # Function to find the length of the longest string in the list
    max_length = 0
    longest_string = ""
    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
            longest_string = string
    return longest_string
# Unit tests
strings = ["apple", "orange", "banana"]
print("Longest string:", longest(strings))
```