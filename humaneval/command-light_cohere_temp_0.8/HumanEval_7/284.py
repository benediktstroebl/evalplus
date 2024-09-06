```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Example usage:
strings = ["abc", "bacd", "cde", "array", " sushi"]
sub = "a"
result = filter_by_substring(strings, sub)
print(result)  # Expected output: ['abc', 'bacd', 'array']
```
This script defines a function `filter_by_substring` that filters a list of strings based on a given substring. The function iterates through each element in the input strings to check if the substring is present, and returns the resulting filtered list.