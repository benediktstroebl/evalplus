```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    elements that should be numbers
    """
    # sort the list
    l = sorted(l)

    # first element is negative
    if l[0] < 0:
        # check for two equal elements
        for i in range(1, len(l)):
            if l[i] == l[i - 1]:
                return False
        else:
            break

    # first element is positive
    elif l[0] > 0:
        # check for two equal elements
        for i in range(1, len(l)):
            if l[i] == l[i - 1]:
                return False
        else:
            break

    # no two equal elements found
    return True
```