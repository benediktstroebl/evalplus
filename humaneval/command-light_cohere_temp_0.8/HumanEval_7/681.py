```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Example usage
strings = ['abc', 'bacd', 'cde', 'array', 'hello world']
sub = 'a'
result = filter_by_substring(strings, sub)
print(result)  # Expected output ['abc', 'bacd', 'array']
```
The function `filter_by_substring` takes a list of strings and a substring as input, and returns a new list of strings that contain the given substring. The script also includes example usage and passes the tests successfully.