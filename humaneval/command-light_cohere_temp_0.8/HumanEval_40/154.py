```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> test_sum_to_zero([1, 3, 5, 0])
    assert triples_sum_to_zero([1, 3, 5, 0]) == True

    >>> test_sum_to_zero([1, 3, -2, 1])
    assert triples_sum_to_zero([1, 2, 3, 7]) == False

    >>> test_sum_to_zero([2, 4, -5, 3, 9, 7])
    assert triples_sum_to_zero([1]) == False

    """

def test_sum_to_zero():
    return [1, 3, 5, 0]

# Main program
l = test_sum_to_zero()
print( triples_sum_to_zero(l) )
```