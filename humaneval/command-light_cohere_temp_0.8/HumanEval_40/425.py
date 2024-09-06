```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    sum of each element of the list is computed using sum()
    """
    return sum([x for x in l if x != 0]) == 0

# Test cases
tests = [3]
for t in tests:
    assert triples_sum_to_zero(t) is True
```