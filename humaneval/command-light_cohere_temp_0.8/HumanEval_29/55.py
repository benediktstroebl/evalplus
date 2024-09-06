Here is a Python script with a self-contained function that solves the problem you described and passes the corresponding tests:

```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]


# Test cases
strings = ['abc', 'bcd', 'cde', 'array', 'hello']
prefix = 'a'

print(filter_by_prefix(strings, prefix))  # Output: ['abc', 'array']
```

In this script, the function `filter_by_prefix` filters a list of strings based on a given prefix. It uses the precise type hint for better code readability and type checking. The test cases demonstrate the valid inputs and the expected output of the function.