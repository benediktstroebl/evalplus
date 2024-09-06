```python
def sort_even(lst):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted."""
    lst[0] = int(lst[0])  # Set the first element as even index
    lst[1] = int(lst[1])  # Set the second element as even index
    lst[2:] = sorted(lst[2:])  # Sort the rest of the list
    return lst
# Example usage:
even_ = [5, 6, 3, 4]
result = sort_even(even)
assert even == result  # Test the result against the original even list

```
This function is self-contained and takes a list lst as input, and returns a new list lst with the elements of the original list sorted according to the desired property.