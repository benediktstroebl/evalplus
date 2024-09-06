```python
def sort_third(l: list):
    """Sorts the list l such that all numbers greater than 3 are at the beginning.
    Numbers greater than a and numbers less than 3 are at the end. Numbers less than than the and numbers divisible by 3 are in between.
    >>> sort_third([1, 2, 3])
    [3, 2, 1]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 1, 2, 3, 4, 5])
    [1, 2, 3, 4, 10]
    >>> sort_third([11, 12, 13, 14, 3, 4, 5])
    Traceback (most recent call last):
    ...
    TypeError: 'int' object does not support item assignment
    --> (45) in <body at 0x__exit__()
    ```