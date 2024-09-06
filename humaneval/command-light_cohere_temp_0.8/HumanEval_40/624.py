```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    Test case: 
    Input: [1, 3, -2, 1] 
    Expected Output: True
    """
    if sum(l) == 0:
        return True
    else:
        return False
```