```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string Count overlapping cases."""
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test case
test_cases = [['', 'aa', 'aaaa'], ['aaaaa']]
for case in test_cases:
    actual = how_many_times(*case)
    expected = len(case)
    assert actual == expected
```