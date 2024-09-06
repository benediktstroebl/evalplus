```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]


# Test cases
strings = ['abc', 'bcd', 'cde', 'array', ' welcome']
prefix = 'array'
print(filter_by_prefix(strings, prefix))  # Output: ['array']
```
This Python script defines a function `filter_by_prefix` that filters a list of strings based on a given prefix. It uses the test a basic string matching algorithm to achieve this.