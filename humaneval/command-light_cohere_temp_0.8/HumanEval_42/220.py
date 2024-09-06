```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    for i in range(n):
        l[i] = l[i] + 1
    return l

# Test the function with a range of inputs
test_list = [1, 2, 3]
test_result = incr_list(test_list)
print("Test 1 result:", test_result)

test_list2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result2 = incr_list(test_list2)
print("Test 2 result:", test_result2)

test_list3 = [5, 2, 5, 2, 3, 3, 8, 2]
test_result3 = incr_list(test_list3)
print("Test 3 result:", test_result3)
```
The code defines a function `incr_list` that takes a list `l` as an argument and returns a new list with elements from the original list incremented by 1. It then proceeds to test the list with a range of values and prints the results.