Here's the Python script with a self-contained function that solves the problem of finding three elements in a list that sum to zero:
```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """

    # Initialize a dictionary to store the sum of each element.
    sums = {x = 0}
    # Loop through the list and calculate the sum of each element.
    for i, element in l:
        sums[i] = sums[i] + element
    # Check if there are three distinct elements in the list that sum to zero
    for i in range(3):
            if sums[i] == 0:
                return True
    return False
```

This script defines a function `triples_sum_to_zero` that takes a list of integers as input and returns `True` if there are three distinct elements in the list that sum to zero, and `False` otherwise.  The `sums` dictionary is used to store the sum of each element, and the function iterates through the list to calculate the sum of each element.