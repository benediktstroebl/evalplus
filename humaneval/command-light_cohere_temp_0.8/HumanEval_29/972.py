```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filter an input list of strings only for ones that start with a given prefix"""
    return [s for s in strings if s[0:] == prefix]


# Test case 1: Filtering strings that start with 'a'
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))
# Expected output ['abc', 'array']


# Test case 2: Filtering strings that start with 'geeks'
print(filter_by_prefix(['geeks', 'coding', 'python', 'aldrich'], 'geeks'))
# Expected output ['geeks']


# Test case 3: Filtering strings that start with 'pro'
print(filter_by_prefix(['pro', 'app', 'lib', 'progs'], 'pro'))
# Expected output ['pro']
```

This Python script provides a self-contained function `filter_by_prefix` that takes a list of strings and a prefix as arguments. It then returns a universal functions are designed to perform specific tasks, such as filtering elements from a collection based on a given criterion.