```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```
The function `filter_by_substring` in this script accepts a list of strings and a substring as inputs. It loops through each substring within each string in the input list to generate a new list containing just the strings that include the substring.