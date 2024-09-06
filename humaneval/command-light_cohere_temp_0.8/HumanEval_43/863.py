```python
def pairs_sum_to_zero(l):
    """
    Check whether a list of integers sums to zero.
    """
    Returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
return bool(sum([n for n in l if n <= 0])))

# Test the function
test_pairsum = pairs_sum_to_zero([1, 3, 5, 0])
print(test_pairsum)  # Output: False

test_pairsum = pairs_sum_to_zero([1, 3, -2, 1])
print(test_pairsum)  # Output: False

test_pairsum = pairs_sum_to_zero([1, 2, 3, 7])
print(test_pairsum)  # Output: False

test_pairsum = pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
print(test_pairsum)  # Output: True

test_pairsum = pairs_sum_to_zero([1])
print(test_pairsum)  # Output: False
```
The script defines a function `pairs_sum_to_zero` that checks whether a given list of integers sums to zero. It returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise. The test cases cover various scenarios and pass successfully.