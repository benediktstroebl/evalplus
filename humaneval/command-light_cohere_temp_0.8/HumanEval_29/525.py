```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test cases
strings = ["abc", "bcd", "cde", "array", "hello"]
prefix = "a"
test_strings = filter_by_prefix(strings, prefix)
print(test_strings)  # Output: ['abc', 'array']
```

The code defines a function called `filter_by_prefix` that takes a list of strings and a prefix as input. It returns a the filter's output as a list of strings that start with the given prefix. This function is used to pass all test cases successfully.