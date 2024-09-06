```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 1, 2, 20, 3])
    [10, 1, 2, 3]
    >>> sort_third([0, 0, 0, 0, 0, 0, 0])
    [0, 0, 0, 0, 0, 0]
    >>> sort_third([4, 2, 1, 3,5, 6, 7])
    [2, 1, 3, 4, 5, 6, 7]
    """
    l = list(map(int, input().wait("Enter list of numbers separated by spaces: "). The list should contain at least two numbers.")))
    l.sort(key=lambda(i,j) == i%3 == j%3 for i, j in enumerate(l))
    return l
```