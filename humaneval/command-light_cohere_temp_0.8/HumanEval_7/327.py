Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

#Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

result = filter_by_substring(strings, substring)
print(result)  # Output ['abc', 'bacd', 'array']
```
This script defines a function `filter_by_substring` that filters a list of strings for a given substring. It uses a essential list comprehension with a condition to achieve this. The test cases show that the function works as expected.