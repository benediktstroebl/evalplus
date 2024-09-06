```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for char in substring if char in string)

# Test cases
test_cases = [
    ("", "a")
    ("aaa", "aa"),
    ("aaaa", "aa"),
    ("aaaaaa", "aa"),
    ("hello", "el"),
    ("world", "uorwld")
]

for test in test_cases:
    assert how_many_times(test[0], test[1]) == len(test[0])
```