```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Testing the function with sample inputs
strings = ["abc", "bacd", "cde", "array", "adfas"]
substring = "a"

# Expected output: ['abc', 'bacd', 'array']
result = filter_by_substring(strings, substring)

print(result)
``` 
The code defines a function called `filter_by_substring` that takes two parameters: a list of strings and a substring. The function uses a loop to iterate over each string in the input list and returns the string if the substring is found in the current string.