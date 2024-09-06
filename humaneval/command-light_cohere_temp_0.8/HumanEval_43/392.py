```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    for i in l:
        if sum(i) == 0:
            return True
        else:
            return False
    """

# Test the function
test_result = pairs_sum_to_zero([1, 3, 5, 0])
test_result = pairs_sum_to_zero([1, 3, -2, 1])
test_result = pairs_sum_to_zero([1, 2, 3, 7])
test_result = pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
test_result = pairs_sum_to_zero([1])

print(test_result)
```