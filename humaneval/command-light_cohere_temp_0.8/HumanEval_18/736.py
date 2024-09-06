```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for char in substring if char in string)

# Test cases
test_cases = [
    ("", "a"), ("aaa", "aaaay"),
    ("aaaa", "aa"), ("aaaa", "aaa"),
    ("aaaa", ""), ("aaaa", "aaaaaa") # Overlapping case
]

for test_case in test_cases:
    actual = how_many_times(test_case, "a")
    assert actual == len(test_case)
```