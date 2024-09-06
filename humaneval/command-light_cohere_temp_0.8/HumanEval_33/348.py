```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted."""
    return [x if x%3==0 else x-3 for x in l]

# Test the function
test_list = [5, 6, 3, 4, 8, 9, 2]
test_list_sorted = sort_third(test_list)
assert test_list == test_list_sorted
```