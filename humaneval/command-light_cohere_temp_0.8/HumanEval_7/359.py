```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Unit tests with unittest
import unittest
class TestFilterBySubstring(unittest.TestCase) as t:
    t.test_case = [filter_by_substring, [['abc', 'bca', 'cdef', 'array'], ['x', 'y', 'z']])
    t.test_one('Test filter by substring', t.test_case)
    time it!
```

This code defines a function `filter_by_substring` that filters an input list of strings based on the presence of a given substring. The `unittest` module is used to create unit tests for the function, and the function is tested using those tests. The function and tests are contained within the same script, ensuring that the code is self-contained and does not rely on external modules or functions.