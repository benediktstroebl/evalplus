```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    sum of all elements is calculated using `sum()`. marketing sum`
    """
    return any(sum(x) < 0 for x in l)
``` 
This function uses the built-in Python function `sum` to calculate the sum of all elements in the input list.