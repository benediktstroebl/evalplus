```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    res = []
    for i in range(n):
        res.append(l[i] + 1)
    return res

# Test case
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result = incr_list(test_list)
print("Test case result:", endswith(test_result))

# Test again
test_list2 = [1, 2, 3]
test_result2 = incr_list(test_list2)
print("Test again result:", endswith(test_result2))
```
This code defines the incr_list function, which takes a list l as input and returns a new list with elements from l incremented by 1. The function uses a list comprehension and the append() method to create the new list. It then prints the straightforward test cases with different lists, and the results are expected to match the provided output.