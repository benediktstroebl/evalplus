```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "text"]
substring = "a"

# Function call and print results
print(filter_by_substring(strings, substring))
``` 
The function will filter out and return the strings that contain the specified substring.