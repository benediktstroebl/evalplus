```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted."""
    return sorted(l, key = lambda x: x if x % 2 else x // 2)

# tests
test_list = [1, 2, 3]
test_list2 = [5, 6, 3, 4]

# call function and check the result
print(sort_even(test_list)) == [1, 2, 3] )
print(sort_even(test_list2)) == [3, 6, 5, 4] )
```