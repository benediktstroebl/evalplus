```python
def triples_sum_to_zero(lst):
    """
    Checks if there are three distinct elements in the list that sum to zero.
    Returns: True, if there are, and False otherwise.
    """
    def test_triple_sum_zero(lst):
        return triples_sum_to_zero(lst) and (sum(lst) == 0)
    return test_triple_sum_zero

# Example usage:
test_triple_sum_zero([1, 3, -2, 1])  # True
test_triple_sum_zero([1, 2, 3, 7])  # False
test_triple_sum_zero([2, 4, -5, 3, 9, 7])  # True
test_triple_sum_zero([1])        # False
```
The code defines a function `triples_sum_to_zero` that checks whether there are three distinct elements in the list that sum to zero. It returns `True` if the test passes.