```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """

    list of numbers should be positive
    """
    if not all(n >= 0 for n in l):
        return False

    s = 0
    for i in range(len(l)):
        s += l[i]
        if s < 0:
            return False
    return True
```