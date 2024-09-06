```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from `strings` that have the specified `prefix`. The resulting list is then typed as `List[str]` to convey that it contains only strings. 

To ensure each argument's correctness, here is a test script to accompany the function:
```python
from typing import List

def test_filter_by_prefix():
    # Test case 1: Empty list, non-empty prefix
    assert not filter_by_prefix([], "a")

    # Test case 2: List with matches, non-empty prefix
    assert filter_by_prefix(["abc", "bcd", "cde", "array"], "a") == ["abc", "array"]

    # Test case 3: List with matches, empty prefix
    assert filter_by_prefix(["abc", "bcd", "cde", "array"], "") == ["abc", "bcd", "cde", "array"]

    # Test case 4: List without matches, empty prefix
    assert not filter_by_prefix(["123", "456", "789"], "abc")

test_filter_by_prefix()
```

In the above test script, the `test_filter_by_prefix()` function verifies the behavior of the `filter_by_prefix()` function for different scenarios. 

1. `assert not filter_by_prefix([], "a")` tests the case where an empty list is passed with a non-empty prefix, expecting an empty list as output.
2. `assert filter_by_prefix(["abc", "bcd", "cde", "array"], "a") == ["abc", "array"]` tests the case where a list contains strings with a specific prefix, expecting a list with only the matched strings.
3. `assert filter_by_prefix(["abc", "bcd", "cde", "array"], "") == ["abc", "bcd", "cde", "array"]` tests the case where keeping all strings in the list, regardless of whether they start with a prefix, is required. 
 4. `assert not filter_by_prefix(["123", "456", "789"], "abc")` tests the case where no strings in the list start with the given prefix, expecting an empty list as output. 

The final `test_filter_by_prefix()` function is called to run through all the test cases and validate the `filter_by_prefix()` function.