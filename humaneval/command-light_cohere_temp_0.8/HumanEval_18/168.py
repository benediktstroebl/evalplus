```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for char in string if char == substring)

# Test the function with various inputs
test_cases = [
    ("", "a")
    ("aaa", "a")
    ("aaaa", "aa")
    ("aaaa", "")
    ("abcde", "de")
    # Long string with random characters
]

for text, sub in test_cases:
    result = how_many_times(text, sub)
    assert result == len(sub) in text

print("All tests passed!")
```