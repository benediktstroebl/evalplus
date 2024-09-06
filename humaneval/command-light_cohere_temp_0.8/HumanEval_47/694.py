```python
def median(l):
    # Sort the list
    l.sort(l)
    # Return the sorted list as the median
    return l[-1]

# Test cases
test = [
    [(-10, 4, 6, 1000, 10, 20), 3, 0, 1, 2, 5, 4, 6, 15)]

for test_case in test:
    assert median(test_case) == test_case[-1]
```