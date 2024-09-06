```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Unit tests
strings = ["abc", "bacd", "cde", "array", "hello"]
substrings = ["a", "band", "cde"]

# Test case 1
test_case1 = [filter_by_substring(strings, substrings)]
assert test_case1 == ['abc', "bacd", "array"]

# Test case 2
test_case2 = [filter_by_substring(strings, "band")]
assert test_case2 == []

# Test case 3
test_case3 = [filter_by_substring(strings, "a")]
assert test_case3 == ['abc', "bacd", "array"]

# Test case 4
test_case4 = [filter_by_substring([

        "abc"a"
        "bca"
    ], "a")]
assert test_case4 == ["abc"a"]
```

This Python code defines a function `filter_by_substring` that filters a list of strings for a given substring. The function uses a string method `in` to check if each string contains the substring. It tests the creating a list of strings and a string to test the function.

The code also includes unit tests to validate the function's behavior. They use the `assert` to check if the output of the `filter_by_substring` function matches the expected result for different input scenarios.