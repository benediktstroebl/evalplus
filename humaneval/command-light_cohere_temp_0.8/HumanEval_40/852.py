```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    test and returns True.

    -1 2 3, -1;3;5;0  # Should return True
    -1 2 3; -2;1  # Should return False
    -4 5 6; -4;5  # Should return False
    -2 3 4; -2;6  # Should return True
    """
    set sum = 0
    for num in l:
        if set sum > 0:
            set sum += num
    else:
        return False
    return True
```