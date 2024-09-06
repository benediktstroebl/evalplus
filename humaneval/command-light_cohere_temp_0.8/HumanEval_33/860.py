```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    return sorted(l, key=lambda x: not_divisible(x, 3))

def not_divisible(x: int, m):
    """This function takes an integer x and an integer m, and returns
    True if x is divisible by m, else returns False."""
    return x % m == 0
```
The provided script defines a function `sort_third` that sorts a list according to the values that are not divisible by three. The function uses another function, `not_divisible`, to identify these values and ensures that the corresponding values in the list are equal. The function then uses the Python's built-in `sorted` function to sort the list.

Note that the function `not_divisible` is not included, it's just an example of how you can create your own function.  The way to implement your specific logic for identifying the values that should be treated as not divisible by three.