```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Example usage:
strings = ['abc', 'bacd', 'cde', 'array', 'hello world']
substring = 'a'
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```
The function `filter_by_substring` takes a list of strings and a substring as input and returns a new list of strings that contain the given substring. 


The function uses a list comprehension to iterate over each string in the input list and checks if the substring is present in the string.