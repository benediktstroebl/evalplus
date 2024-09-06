```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> test_triples_sum_to_zero([1, 3, 5, 0])
    """
    return (sum(set(map(int, l)))) == 0
```