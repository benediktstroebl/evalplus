```python
def sort_third(l: list):
    """Sorts a list of integers so that numbers divisible by three appear first.

    >>> sort_third([1, 2, 3])
    [1, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 3, 4, 6, 8, 9]
    """
    return sorted(l, key=lambda x: not_divisible(x, 3))

def not_divisible(x, y):
    return (x // y) == 0
```
This Python script defines a function `sort_third` that sorts a list of integers such that numbers divisible by three appear first. It employs another function `not_divisible` that checks if a given number is divisible by a specific divisor. The `sort_third` function then sorts the list based on this divisor, ensuring that numbers divisible by three are placed first.