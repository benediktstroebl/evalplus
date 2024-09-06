```python
def sort_even(lst):
    """This function takes a list l and returns a list l' such that l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted.

    Args:
        lst(list)

    Returns:
        list: l'
    """
    lst[:] = [x if i % 2 == 0 else x[::-1] for i, x in enumerate(lst)]
    return lst

# Test the function
test_even = [1, 2, 3]
test_even.sort_even(test_even)
# Should return [1, 2, 3]

test_even = [5, 6, 3, 4]
test_even.sort_even(test_even)
# Should return [3, 6, 5, 4]
```