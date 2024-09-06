```python
def how_many_times(string: str, substring: str) -> int:
    """
    Counts how many times a given substring can be found in the original string, with overlapping cases.
    >>> string = "aaaaaaa"
    sub = "aa"
    count = how_many_times(string, sub)
    print(f"The substring {sub} can be found {count} times.")
    return count

# Test cases
test_cases = [
    ("", "a"),
    ("aaa", "a"),
    ("aaaa", "a"),
    ("aaaa", "aa"),
    ("aa", "aaa"),
    ("aaaa", "aaa"),
    ("aa", "aaaa"),
    ("aaa", "aaaaaa"),
    ("bbbb", "bbbb"),
    ("bbbb", "bbbb"),
    # Not valid input
]

for test_case in test_cases:
    got_count = how_many_times(test_case[0], test_case[1])
    print(f"Test case {test_case}: {got_count}, should be {test_case[1]}")
```