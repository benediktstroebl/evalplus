```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    """
    return sum([x for x in l if len(set([x])) == 3]) == 0

# Test cases
tests = [
    [
        [1, 3, 5, 0],
    ]
)

for test in tests:
    result = triples_sum_to_zero(test)
    assert result == True
```