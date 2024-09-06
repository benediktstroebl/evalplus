```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring in the original string.
    >>> how_many_times('aa', 'a')  # Result: 0
    >>> how_many_times('aaaaaa', 'aa')  # Result: 3
    """
    return sum(1 for w in string.find(substring, string) if substring in w)

# Test cases
test_cases = [
    ("aa",)
    ("aaaaaa",)
    (os.join("aa"),)
]

for string, test in test_cases:
    result = how_many_times(string, test)
    assert result == len(string.find(test, string))
```