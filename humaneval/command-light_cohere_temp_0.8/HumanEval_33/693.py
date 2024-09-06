```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.

    Test cases on the test_third([1, 2, 3])
    [1, 2, 3]
    >>> test_sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> test_sort_third([10, 2, 3, 1, 4])
    [1, 2, 3, 4, 10]
    """
    l = list(l)
    l.sort_indic = sorted(l, key=lambda x: not_divisible(x))
    l = l[:] + l[-1:]
    return l

def not_divisible(x):
    """Check if x is divisible by 3."""
    return x % 3 == 0
```