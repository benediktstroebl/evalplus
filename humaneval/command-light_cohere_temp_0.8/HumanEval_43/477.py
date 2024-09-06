```python
def pairs_sum_to_zero(l):
    return any(x+y <= 0 for x, y in zip(l, l[1:]))

# Test the function
test_result = pairs_sum_to_zero([1, 3, 5, 0])
assert test_result == False

test_result = pairs_sum_to_zero([1, 3, -2, 1])
assert test_result == False

test_result = pairs_sum_to_zero([1, 2, 3, 7])
assert test_result == False

test_result = pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
assert test_result == True

# Additional test cases
test_result = pairs_sum_to_zero([1])
assert test_result == False

test_result = pairs_sum_to_zero([])
assert test_result == True
```
The function checks if any element in the list added to the previous element will result in a negative sum, and returns `True` if this condition is met, indicating that the list has two elements whose sum is zero.  Otherwise, it returns `False` if no such element satisfies this condition.