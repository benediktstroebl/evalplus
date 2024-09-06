```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    for i in range(n):
        l[i] = l[i] + 1
    return l

#Test cases
test_incr_list = []
test_incr_list.push([1, 2, 3])
test_incr_list.push([5, 5, 3, 5, 2, 3, 3, 9, 0, 123])

#Test results
test_results = incr_list(test_incr_list)
print("Test Results:", test_results)
```