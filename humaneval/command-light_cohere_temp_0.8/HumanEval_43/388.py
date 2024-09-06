```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list comprehension is the logic of the sum of two integers in the list being zero:
    ```python
    for a, b in l:
        if a + b <= 0:
            return True
    return False
    ```