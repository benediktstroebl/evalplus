```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Return the longest string from a list of strings.
    Args:
    strings (List[str]): List of strings
    Returns:
    List[str]: the longest string
    """
    if not strings:
        return None

    return max(strings, key=len)

# Unit test
test_longest = []
test_longest.append(['a', 'b', 'c'])
test_longest.append(['bb', 'ccc'])
test_longest.append(['aa', 'ccc'])
test_longest.append([None])
test_longest.append([])
test_longest.append(['ab'])
print(test_longest)
```