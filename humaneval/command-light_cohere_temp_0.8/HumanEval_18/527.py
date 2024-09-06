```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in substring:
        if char == string[count]:
            count += 1
    return count

# Test suite
test_cases = [
    ("', 'a')
    ("aaa", "aa")
    ("aaaa", "aa")
    ("abc", "abc")
    ("abcd", "abcd")
]

for test in test_cases:
    assert how_many_times(test[0], test[1]) == len(test[1])
```