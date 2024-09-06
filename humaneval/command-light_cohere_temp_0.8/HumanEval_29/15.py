```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Test cases
strings = ['abc', 'bcd', 'cde', 'array', 'hello', 'world']
prefix = 'array'
print(filter_by_prefix(strings, prefix))  # Output: ['array']
```
The function `filter_by_prefix` takes two parameters - a list of strings and a prefix string. It uses the list comprehension to filter the strings from the input list that starts with the given prefix. The test case demonstrates how the can pass the test.