```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted."""
    return [x for x in l if x % 3 == 0] + [x for x in l if x % 3 != 0]

# Test the function with a list of numbers
test_list = [5, 6, 3, 4, 8, 9, 2]
result = sort_third(test_list)
assert result == [2, 6, 3, 4, 8, 9, 5]
result = sort_third([10, 11, 12, 13, 14, 15, 16])
assert result == [12, 13, 14, 15, 16, 11, 10]
```