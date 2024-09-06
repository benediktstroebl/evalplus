```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted."""
    l[:] = [x if x % 2 == 0 else x[::-1] for x in l]
    return l
# Example usage
test_list = [5, 6, 3, 4]
result = sort_even(test_list)
assert result == [3, 6, 5, 4]
```