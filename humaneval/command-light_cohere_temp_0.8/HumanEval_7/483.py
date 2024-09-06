```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Unit tests
strings = ["abc", "hello", "world", "abc", "123"]
substrings = ["a", "bc", "123"]

test_strings = [f"filter_by_substring(strings, substrings) for substrings in substrings]

test_lists = [test_strings[0], test_strings[1]]
test_output = ["abc", "hello"]

# Validate function behavior
assert(test_lists == test_output, "Expected: {extra_output} but was {test_output}")
``` 
This code defines a function `filter_by_substring` that filters a list of strings for those that contain a given substring.  It takes output of this code is a test suite that validates the correctness of the function, ensuring it returns the correct results for a given input of strings and substrings.