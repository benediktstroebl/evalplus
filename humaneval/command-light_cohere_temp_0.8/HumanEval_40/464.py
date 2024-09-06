```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> return True if l=[1, 3, -2, 1]
    """
    if sum(l) == 0:
        return True
    return False

# Test cases
test_pass = triples_sum_to_zero([1, 3, -2, 1])
test_fail = triples_sum_to_zero([1, 2, 3, 7])
test_big = triples_sum_to_zero([2, 4, -5, 3, 9, 7])
test_empty = triples_sum_to_zero([])
print("Test results:")
```