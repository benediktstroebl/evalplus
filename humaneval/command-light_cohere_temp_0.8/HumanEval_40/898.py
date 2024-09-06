```python
def triples_sum_to_zero(l):
    """
    Check if all three elements in the list sum up to zero.
    Returns: True if all three integers are distinct, and sum is zero, and False otherwise.
    """
    returns: bool
"""
    return sum((x for x in l)) == 0 and len(set(l)) == 3

# Tests
def test_triples_sum_to_zero():
    """
    Tests the function 'triples_sum_to_zero'

    >>> test_triples_sum_to_zero()
    True
    >>> test_triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> test_triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> test_triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> test_triples_sum_to_zero([1])
    False
    """
# Main execution
test_triples_sum_to_zero()
```