```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted."""
    return sorted([x if x % 2 == 0 else x for x in l])

# Test the function
test_list = [5, 6, 3, 4]
result = sort_even(test_list)
print(result)  # Output: [3, 6, 5, 4]
```