```python
def incr_list(lst):
    lst[::] += 1  # Using list unpacking syntax
    return lst

# Test cases
tests = [
    [1, 2, 3],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [100, 20, 30]
]

for test in tests:
    actual = incr_list(test)
    assert actual == test  # Assert the result matches the expected list
```