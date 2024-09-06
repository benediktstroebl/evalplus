```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the odd indic, while its values at the even indicies are equal to the values of the even indic of l, but sorted."""
    return [x if x%2==0 else x[::-1] for x in l]

# Test the function
tests = [5, 6, 3, 4]
tests = sort_even(tests)
print(tests)
```