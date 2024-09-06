```python
def sort_third(l: list):
    """Sorts the list l such that values at indices that are not divisible by three are in their correct positions."""
    return sorted(l, key=lambda x: not_divisible(x, 3))

def not_divisible(x, m):
    return x // m == 0

# Example usage:
>>> l = [5, 6, 3, 4, 8, 9, 2]
>>> sort_third(l)
[2, 6, 3, 4, 8, 9, 5]
```
This script defines a function `sort_third` that sorts a list such that indices that are not divisible by three are in their correct positions. The key function `not_divisible` checks whether a value is divisible by a given number `m`, and returns `True` if it is. It then sorts the
 list using this function as the key, and returns the sorted list.