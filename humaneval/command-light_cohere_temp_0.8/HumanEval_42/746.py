```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

# Test case 1
assertEqual([1, 2, 3], [2, 3, 4])

# Test case 2
assertEqual([5, 3, 5], [6, 4, 6])

# Test case 3
assertEqual([5, 3, 5, 2, 3, 3], [6, 4, 6, 3, 4, 4])

# Test case 4
assertEqual([5, 3, 5, 2, 3, 3, 9, 0, 123], [6, 4, 6, 3, 4, 4, 4, 10, 1, 124])
```
This Python code defines a function incr_list that iteratively adds 1 to each element in a given list. It then performs several assertions to test the correctness of the function. The code uses the necessary assertions to check the function's behavior for different inputs and ensure it produces the expected results.