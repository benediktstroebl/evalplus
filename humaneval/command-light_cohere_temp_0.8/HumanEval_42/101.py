```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    for i in range(n):
        l[i] = l[i] + 1
    return l

# Test
test_incr_list = incr_list([1, 2, 3])
print("Test 1:", test_incr_list)  

test_incr_list = incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
print("Test 2:", test_incr_list)

```
This script defines a function `incr_list` that takes a list `l` as an argument and returns a new list with elements from the original list incremented by 1. The test code creates two test cases using the function, and the results are printed to the console.