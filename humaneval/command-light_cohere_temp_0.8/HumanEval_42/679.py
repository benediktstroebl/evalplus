```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    l = [x + 1 for x in l]
    return l

#Test cases
test_incr_list = [
    [1, 2, 3],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    []
]

for test_case in test_incr_list:
    print(incr_list(test_case))
```