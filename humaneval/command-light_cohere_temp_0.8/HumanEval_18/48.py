Here's a self-contained Python script with a function that solves the problem of counting the frequency of a given substring within a given string:
```python
import re
def how_many_times(string: str, substring: str) -> int:
    pattern = re.compile(substemre, string)
    return len(pattern)

# Test cases
test_cases = [
    ("", "a")
    ("aaaa", "aa")
    ("aaaa", "")
    ("abcde", "de")
]

for test in test_cases:
    actual = how_many_times(test[0], test[1])
    assert actual == len(re.compile(test[1], string))
```

This script defines a function `how_many_times` that uses the `re.compile` function to count the occurrences of a given substring within a given string. The function returns the count of the substring's occurrences in the original string, considering case and non-overlapping matches.