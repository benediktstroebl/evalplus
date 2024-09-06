Here is a Python script that contains a self-contained function to solve the problem:
```python
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    s = 0
    for i in l:
        s += i
    return s == 0
```
The script defines a function `triples_sum_to_zero` that takes a list `l` as input and returns `True` if the list contains three distinct elements whose sum is equal to zero, and `False` otherwise. The function utilizes a `s` to sum the elements of the list, and checks if the sum equals zero.