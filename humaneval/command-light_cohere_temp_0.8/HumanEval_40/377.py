```python
def triples_sum_to_zero(lst):
    """
    Checks if there are three distinct elements in the list that sum to zero.
    Returns: True if they, False otherwise.
    """
   
    tests if there are three elements in the list that sum to zero:
        test_sum_zero([1, 3, 5, 0]) 
        test_sum_zero([1, 3, -2, 1]) 
        test_sum_zero([2, 4, -5, 3, 9, 7]) 
        test_sum_zero([1]) 
    """
    return sum(lst) == 0
```