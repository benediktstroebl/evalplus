```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    length_ss = len(substring)
    for i in range(len(string)):
        if string[i:i+length_ss] == substring:
            count += 1
    return count

# Test cases
test_cases = [
    ("', 'a'),  # Not found
    ("aaa", 'a'),  # Found
    ("aaaa", "aa"), # Found
    ("abcde", "de"), # Not found
]

for test_case in test_cases:
    actual = how_many_times(test_case[0], test_case[1])
    assert actual == len(test_case)
```