```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i, char in enumerate(string):
        if char == substring:
            count += 1
    return count

# Test the function
test_how_many_times = {}
test_how_many_times[''] = 0
test_how_many_times['aa'] = 3
test_how_many_times['aaaa'] = 3

print(test_how_many_times)
```