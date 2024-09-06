```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted.
    """
    list comprehension, filtering even indices and mapping even indices to the corresponding values.

l = [1, 2, 3, 4, 5, 6]
l = sort_even(l)
print(l)
```