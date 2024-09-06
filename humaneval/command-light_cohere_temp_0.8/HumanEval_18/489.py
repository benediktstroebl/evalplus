```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for char in substring if char in string)

# Test cases
test_cases = [
    ("", "")  # empty string
    ("abc", "a")  # match
 , ("abc", "ab")  # match
 , ("hello", "el")  # no match
 , ("bob", "ob")  # match
]

for t, s in test_cases:
    actual = how_many_times(s, t)
    assert actual == len(s)
```