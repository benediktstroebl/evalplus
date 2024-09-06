```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in substring:
        if char in string:
            count += 1
    return count

# Test the function with some examples
test_how_many_times = {}
test_how_many_times[''] = [0, 3]
test_how_many_times['aaa'] = [3, 3]
test_how_many_times['aaaa'] = [3, 3]

for result in test_how_many_times.values():
    result:
    assert how_many_times(result[0], result[1]) == result[2]
```