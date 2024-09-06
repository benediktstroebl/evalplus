```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted."""
    l[:2] = [x for x in l[1:]] + [l[0]]
    return l
# Example usage
l = [5, 6, 3, 4]
print(sort_even(l))
```