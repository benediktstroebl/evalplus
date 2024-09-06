```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for i, char in enumerate(string) if char == substring)

# Test the function with various cases
test_cases = [
    ("", "a"), 
    ("aaaa", "aa"),
    ("", "")
]

for test in test_cases:
    assert how_many_times(test, "a") == len(test) == 0
```