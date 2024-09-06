```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == float("inf")]

# Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_set = set(test_list)

assert unique(test_list) == test_set
assert set(unique([0, 2, 3, 5, 9, 123])) == set([0, 2, 3, 5, 9, 123])
assert len(unique([float("inf") for _ in range(1000)])) == 1000

# Correct output
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 0, 123, 5]
test_set = set(test_list)

assert unique(test_list) == test_set
```