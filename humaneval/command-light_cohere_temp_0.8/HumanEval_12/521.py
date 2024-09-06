```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    # Initialize the longest length and the longest string
    max_length = 0
    longest_str = ""

    # Compare and update longest length and string
    for string in strings:
        if len(string) > max_length:
            longest_str = string
            max_length = len(string)

    # Return the longest string
    return longest_str if longest_str else None

# Test the function
test_strings = ["a", "bb", "ccc", "xy"]
result = longest(test_strings)
print(result)  # Output: "ccc"
```
This script defines a function `longest` that takes a list of strings and returns the longest string. The function uses a string length and a shared longest string as two variables, and compares them accordingly. Finally, the function returns the longest string.