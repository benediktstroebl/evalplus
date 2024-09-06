```python
from typing import List
def longest(strings: List[str]):
    """ Outlines list of strings, returns the longest string """
    if not strings:
        return None
    return max(strings, key=len)
# Test cases
strings = ['a', 'b', 'c']
print(longest(strings))  # Output: c
strings = ['aa', 'bb', 'ccc']
print(longest(strings))  # Output: bb
strings = []
strings. string longest('abbbccc')  # Output: bbbccc
strings = ['a', 'aa', 'aaaa', 'b', 'c']
print(longest(strings))  # Output: aaaaaa
```

I hope this code demonstrates the implementation of a function named `longest`, which takes a list of strings as input and returns the length of the longest string in the list. The code also provides several test cases to ensure the correctness of the function.