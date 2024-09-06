```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test cases for the function
strings = ['abc', 'bcd', 'cde', 'cdefoo', 'array', 'zxcv']
prefix = 'cde'

# Function call and print results
print(filter_by_prefix(strings, prefix))
```

This script defines a function `filter_by_prefix` that filters a list of strings based on a given prefix. It uses the basic list comprehension to iterate over the input strings and check if each string starts with the given prefix. The function returns a list of matching strings. 

This code is self-contained, and it demonstrates a clear and concise way to solve the problem.