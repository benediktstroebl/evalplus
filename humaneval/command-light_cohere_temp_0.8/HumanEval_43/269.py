```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    function uses the Python's `sum()` function to calculate the sum of all elements in the list.
    It then returns True if the sum is equal to zero, and False otherwise.
# Example the test cases
2

if l[0] > 0 and l[-1] <= 0:
    return True
elif l[0] <= 0 and l[-1] > 0:
    return False
else:
    return False
```