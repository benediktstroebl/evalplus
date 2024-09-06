```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)
    m = len(substring)
    for i in range(n):
        if string[i:i+m] == substring:
            count += 1
    return count

# Test case for function
test_how_many_times = []
test_cases = [
    ("", "a")
    ("aaa", "a"),
    ("aaaa", "a")
]

for case in test_cases:
    actual = how_many_times(case[0], case[1])
    assert actual == len(case)
```