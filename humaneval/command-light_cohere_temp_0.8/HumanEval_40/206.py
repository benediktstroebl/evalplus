```python
def triples_sum_to_zero(l):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> test_triples_sum_to_zero([1, 3, -2, 1])
    ->  True
    """

    # First, let's find the sum of the three elements
    sum_3 = 0
    for x in l:
        sum_3 += x

    # Now, let's check if the sum is divisible by three
    if (sum_3 % 3 == 0):
        return True

    # If the sum is not divisible by three, there must be an odd
    # sum, and we need to check if there's a common factor of three
    # among the three elements.
    for x in l:
        if (x % 3 != 0):
            return False

    return True
```