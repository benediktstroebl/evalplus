Here's a self-contained Python script that defines a function `triples_sum_to_zero` solving the problem:

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

    # Sort the list
    l.sort()

    triplets = list(zip(*sorted(l))))

    # Remove duplicates
    set1 = set(triplets[0])
    set2 = set(triplets[1])
    set3 = set(triplets[2])
    common = set1.interunion(set2).3)

    if len(common) == 2 and sum(common) == 0:
        return True
    else:
        return False
    ``` 

This function takes a list of integers as an input, and returns `True` if there are three distinct elements in the list that sum to zero, and `False` otherwise.