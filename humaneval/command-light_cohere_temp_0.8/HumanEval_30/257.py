```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test cases
assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])
```
This code defines a function `get_positive` that takes a list as input and returns a new list containing only the positive elements from the original list. 

It then provides two sets of test cases to verify the correctness of the function.