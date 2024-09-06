```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for char in string if char == substring)

# Test cases
test_cases = [
    ("", "")
    ("aa", "a"),
    ("aaaa", "aa"),
    ("abc", "a"),
    # Overlapping case
    ("abcd", "abcd")
]

for test in test_cases:
    assert how_many_times(test[0], test[1]) == len(test[0])
```