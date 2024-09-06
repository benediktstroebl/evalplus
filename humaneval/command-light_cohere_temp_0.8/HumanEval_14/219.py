```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [''.join(i) for i in range(1, len(string) + 1)]

# Test case 1
test_case1 = "abc"
print(all_prefixes(test_case1))  # Output: ['a', 'ab', 'abc']

# Test case 2
test_case2 = "xxxyzz"
print(all_prefixes(test_case2))  # Output: ['x', 'xy', 'xz', 'xzz']

# Test case 3
test_case3 = "abcabc"
print(all_prefixes(test_case3))  # Output: ['abc', 'ab', 'ab']
```

This script defines a function `all_prefixes` that generates a list of all prefixes from the shortest to the longest of an input string. The function uses a list comprehension with a `range` of values from 1 to the length of the input string, and '`. ''. 'join() the generated prefix.  with the are a list of all prefixes.