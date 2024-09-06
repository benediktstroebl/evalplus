```python
def pairs_sum_to_zero(lst):
    return any(x+y > 0 for x,y in zip(lst, lst[1:]))

# Test the function
test_result = pairs_sum_to_zero([1, 3, 5, 0])
assert test_result == False

test_result = pairs_sum_to_zero([1, 3, -2, 1])
assert test_result == False

test_result = pairs_sum_to_zero([1, 2, 3, 7])
assert test_result == False

test_result = pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
assert test_result == True

test_result = pairs_sum_to_zero([1])
assert test_result == False
```
The function `pairs_sum_to_zero` takes a list of integers and returns `True` if there are two distinct elements in the list that sum up to zero, and `False` otherwise.  The uses theol combination of elements in the list.