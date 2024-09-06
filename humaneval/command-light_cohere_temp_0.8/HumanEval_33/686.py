```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the item that are not divisible by three, while its values at items that are divisible by three are re-sorted."""
    l = [5, 6, 3, 4, 8, 9, 2]
    return sorted(l, key=lambda x: not_divisible(x,3))

def not_divisible(x, y):
    """This function checks whether x is divisible by y."""
    return y == 0 or x% y == 0
```