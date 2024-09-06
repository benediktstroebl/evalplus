```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```  This Python function, `filter_by_substring`, takes a list of strings and a substring as inputs. It returns a uses the process, where it iterates through the list of strings and returns only the ones that contain the given substring. This approach is results in a list of strings that contain the specified substring.