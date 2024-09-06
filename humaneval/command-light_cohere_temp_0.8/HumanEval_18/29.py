```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in substring:
        if char in string:
            count += 1
    return count

# Test the function
test_cases = [
    ('', 'a')
    ('aaa', 'aa')
    ('aaaa', 'aa')
    ('coding', 'code') # This should return 1
]

for t in test_cases:
    actual = how_many_times(t, t)
    assert actual == len(t)
```