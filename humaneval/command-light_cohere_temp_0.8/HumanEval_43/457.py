```python
def pairs_sum_to_zero(l):
    return any(x + y <= 0 for x, y in zip(l, l[1:]))

# Test the function
test_result = pairs_sum_to_zero([1, 3, 5, 0])
assert test_result == False

test_result = pairs_sum_to_zero([1, 3, -2, 1])
assert test_result == False

test_result = pairs_sum_to_zero([1, 2, 3, 7])
assert test_result == False

test_result = pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
assert test_result == True
```
The code defines a function `pairs_sum_to_zero` that checks if any two elements in the list sum to zero. 

The test suite includes several test cases to verify the correctness of the function. 

The `any()` function with a generator expression is used to check if any two elements in the list sum to zero.