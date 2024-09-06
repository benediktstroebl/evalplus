```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
To solve this problem, we first calculate the sum of all elements in the list using the sum function. Then, we use the filter function to find the two elements whose sum is not equal to zero. If the filter returns True, we return True, indicating that the problem is solved. Otherwise, we return False.
```