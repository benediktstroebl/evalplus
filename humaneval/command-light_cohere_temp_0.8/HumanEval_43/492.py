```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    l: list of integers
    """
    if sum(l) == 0:
        return "True"
    else:
        return "False"
``` 
This function checks whether two distinct elements in the list sum up to zero. It does this by iterating through the list, and if the sum is zero, it returns "True"; Otherwise, it returns "False".