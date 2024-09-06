```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]


# Test cases
strings = ["abc", "bcd", "cde", "array", "hello"]
prefix = "a"

# Output: ['abc', 'array']
print(filter_by_prefix(strings, prefix))

# Test case 2: Return an empty list
strings = []
prefix = "a"

# Output: []
print(filter_by_prefix(strings, prefix))
```
This script defines a function **filter_by_prefix** that takes a list of strings and a prefix as input and returns a new list containing only the strings that start with the given prefix. The test cases are used to verify the functionality of the function. You can add more test cases to test the filter_by_prefix function as needed.