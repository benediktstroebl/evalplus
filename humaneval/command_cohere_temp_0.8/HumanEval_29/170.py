```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from `strings` that start with the `prefix`. It uses a list comprehension, which is a powerful Python idiom for creating new lists by performing a transformation on each item in the existing list. 

To test this function, you can call it with different inputs and assert that the returned list is correctly filtered:
```python
def test_filter_by_prefix():
    assert filter_by_prefix([], 'a') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'ar') == ['array']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'ab') == ['abc']
```

You can then run these tests using the `pytest` framework, which provides a simple way to execute test suites and individual test cases:
```bash
pytest -v
``` 

To ensure that the tests fail when the expected outcome is not met, I will include an `assert` statement with the expected result and the result after applying the function in the test cases. If the test passes, all the `assert` statements will return without errors, indicating that the function works correctly.