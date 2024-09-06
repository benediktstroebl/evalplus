```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> l = [1, 3, 5, 0]
    return_zero = triples_sum_to_zero(l)
    if return_zero:
        print("Returned True")
    else:
        print("Returned False")
    >>> l = [1, 3, -2, 1]
    return_zero = triples_sum_to_zero(l)
    if return_zero:
        print("Returned True")
    else:
        print("Returned False")
    >>> l = [1, 2, 3, 7]
    return_zero = triples_sum_to_zero(l)
    if return_zero:
        print("Returned True")
    else:
        print("Returned False")
    >>> l = []
    return_zero = triples_sum_to_zero(l)
    if return_zero:
        print("Returned True")
    else:
        print("Returned False")
    """

triples_sum_to_zero([1, 3, 5, 0]) #This will return True
```