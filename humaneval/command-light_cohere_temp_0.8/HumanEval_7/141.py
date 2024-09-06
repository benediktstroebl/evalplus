Here's the solution for the problem you described:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]

 ```
test_filter_by_substring = []
test_filter_by_substring.add('abc')
test_filter_by_substring.add('cba')
test_filter_by_substring.add('array')
test_filter_by_substring.add('cde')
test_filter_by_substring.add('bcd')
test_filter_by_substring.add('cdef')
test_filter_by_substring.add('ab13cd')

print(filter_by_substring(test_filter_by_substring, 'a'))
```
This Python function `filter_by_substring` accepts a list of strings and a substring as input. It creates a list of all substrings found in the input list. This solution is concise and efficient, using a generator expression to create the filtered list without creating a new list.