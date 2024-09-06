```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted."""
    return l[:-even(len(l))] + l[-even(len(l)):-1]

def even(n):
    return n // 2

# Test the function
test_sort_even(range(10))
```