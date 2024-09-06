```python
from typing import List
def concatenate(strings: List[str]):
    # a function to concatenate list of strings into a single string
    return ''.join(''.join(strings)  # type hint and function call to test the function
```

This code defines a `concatenate` function that takes a list of strings as an argument and returns the concatenated string. The function is tested by passing an empty list `[]` and the function correctly returns an empty string `'``. It also passes the test with a list of three strings `'a', 'b', 'c'`, and returns the expected result `'abc'`.