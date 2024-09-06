```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Example usage
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result) # ['abc', 'bacd', 'array']
```
The function `filter_by_substring` takes a list of strings and a substring as parameters. It returns a general list of all the strings from the input list that contain the given substring.