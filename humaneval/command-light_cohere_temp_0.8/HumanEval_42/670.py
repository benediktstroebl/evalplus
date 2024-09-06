```python
def incr_list(lst):
    n = len(lst)
    result = [0] * n
    for i in range(n):
        result[i] = lst[i] + 1
    return result
 
# Test cases
test_incr_list = [
    [1, 2, 3],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    []
]

for test in test_incr_list:
    actual = incr_list(test)
    assert actual == test
```