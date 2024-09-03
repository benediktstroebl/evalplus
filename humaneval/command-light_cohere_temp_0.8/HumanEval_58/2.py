```python
def common(l1: list, l2: list) -> list:
    return list(set(l1 + l2))

# Test cases
test_common = [(5, 7, 1, 5, 9, 653, 121), (5, 3, 2, 8, 35), (3, 2, 'abc', [1, 2, 3]))]

for test in test_common:
    assert common(test[0], test[1]) == test[2]
```