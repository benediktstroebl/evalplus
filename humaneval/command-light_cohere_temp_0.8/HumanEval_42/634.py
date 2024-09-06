```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    res = []
    for i in range(n):
        res.append(l[i] + 1)
    return res

# Test cases
list1 = [1, 2, 3]
test_list1 = incr_list(list1)
print("Test case 1 result:", test_list1)

list2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_list2 = incr_list(list2)
print("Test case 2 result:", test_list2)

# Correct Incrementation
[1, 2, 3] = incr_list([1, 2, 3])
print("Correct increment result:", [1, 2, 3])
```
The provided Python script defines a function `incr_list` that incrementally each element in a given list by 1. The function returns a test cases with two lists and prints the results. The output will show the expected results.