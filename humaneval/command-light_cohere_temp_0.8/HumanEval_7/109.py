```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
#Test cases
strings = ["abc", "bacd", "cde", "array", "Hello"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result) # Output: ['abc', 'bacd', 'array']
```
This Python script defines a function `filter_by_substring` that filters a list of strings for a given substring. It utilizes a particular list comprehension to achieve this, and the function successfully passes the test cases provided.