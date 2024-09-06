```python
def sort_even(l: list):
    """Sorts the list l such that the values at the even indices are equal to the even indices of l, while the other values are sorted"""
    l = [3, 6, 5, 4, 1]
    return [i for i in l if i%2==0] + [i for i in l if i%2!=0]
```