```python
def sort_third(l: list):
    """Sorts a list l of integers so that elements not divisible by three are moved last.
    
    Returns aning list l' with the values of the corresponding indices of l that are divisible by three 
    moved to the front, and the remaining values of l moved to the back.
    >>> sorted([1, 2, 3])
    [1, 2, 3]
    >>> sorted([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l = list(map(lambda x: 3 if x % 3 == 0 else x, l))
    return sorted(l)
```