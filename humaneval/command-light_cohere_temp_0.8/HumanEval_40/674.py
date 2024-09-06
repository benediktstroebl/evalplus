```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    test_example usage: triples_sum_to_zero([1, 3, -2, 1])  # True

    """
    if sum(map(int, l)) < 0:
        return True
    else:
        return False
```