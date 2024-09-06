```python
def sort_even(l: list):
    """Sorts a list l such that all the odd indices contain the same value, and the even indices contain the same value, but in sorted order."""
    return [i for i, x in enumerate(l) if x % 2 == 0]

# Test case 1
assert sort_even([1, 2, 3]) == [1, 2, 3]

# Test case 2
assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
```
The function `sort_even` takes a list `l` as an argument and returns a new list `l'` which is a sorted list such that all odd indices contain the same value and the even indices contain the same value but in sorted order.