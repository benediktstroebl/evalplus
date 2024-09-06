```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != -end]

# Example usage
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This Python script defines a function `filter_by_substring` that filters a list of strings based on a given substring. The function uses the search to find instances of the substring in each string and returns the list of matching strings. The provided test usage demonstrates how the string with the substring "a" is passed to the function, and the output is printed to the console.