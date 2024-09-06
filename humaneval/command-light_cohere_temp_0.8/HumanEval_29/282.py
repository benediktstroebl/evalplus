```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]


# Test cases
strings = ["abc", "bcd", "cde", "array", "12345"]
prefix = "a"

print("Test case 1:", filter_by_prefix(strings, prefix))
# Expected output: ['abc', 'array']

print("Test case 2:", filter_by_prefix(strings, prefix))
# Expected output: ['cde']

print("Test case 3:", filter_by_prefix(strings, prefix))
# Expected output: []

print("Test case 4:", filter_by_prefix(strings, 'b'))
# Expected output: []

print("Test case 5:", filter_by_prefix(['a', 'aa', 'aaa'], prefix))
# Expected output: []

print("Test case 6:", filter_by_prefix([1, 2, 3, 'abc'], prefix))
# Expected output: []
```
The provided code demonstrates a function called `filter_by_prefix` that filters a list of strings based on a given prefix. The function uses the filtering technique to select only the strings that begin with the specified prefix. 

This method takes a list of strings and a prefix as input and outputs a new list containing only the strings from the input list that start with the given prefix.