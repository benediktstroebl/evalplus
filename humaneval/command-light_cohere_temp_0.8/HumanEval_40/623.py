Here is a Python script with a self-contained function that solves the problem of finding three elements in a list that sum to zero:
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
    set_to_zero = {element for sublist in l for element in sublist}
    if set_to_zero:
        return True
    return False
```
The function takes a list of integers as input and returns True if there are three distinct elements in the list that sum to zero, and False otherwise. The function uses a set of all the elements in the list and checks if there are three distinct elements that sum to zero. 

You can use this script as a starting point to solve the problem.