```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from the input list that start with the input prefix. The function leverages list comprehension and the `startswith` method to efficiently filter the desired strings from the input list based on the provided prefix. 

To test this function, you can use the following code:
```python
test_list = ['abc', 'bcd', 'cde', 'prefixed_string']
test_prefix = 'pre'

expected_result = ['prefixed_string']

assert filter_by_prefix(test_list, test_prefix) == expected_result
```

The function passes the test if the `assert` statement evaluates to True.