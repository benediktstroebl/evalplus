```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test case 1: Basic strings without prefix
test_case_1 = [ "abc", "bcd", "cde"]
assert filter_by_prefix(test_case_1, "a") == ["abc"]

# Test case 2: Lists and one string with prefix
test_case_2 = ["a", "abc", "cdef", "array", "ab"]
assert filter_by_prefix(test_case_2, "a") == ["abc", "array"]

# Test case 3: List with multiple prefixes
test_case_3 = ["a", "ab", "abc", "abcd", "ac", "ad"]
assert filter_by_prefix(test_case_3, "ab") == ["ab", "abc"]

# Test case 4: Containers with non-strings
test_case_4 = [123, "abc", 45]
assert filter_by_prefix(test_case_4, "abc") == []

print("All tests passed!")
```