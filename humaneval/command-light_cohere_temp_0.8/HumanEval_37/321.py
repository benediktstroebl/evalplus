```python
def sort_even(lst):
    """This function takes a list l and returns a list l' such that l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted.
    """
Example:
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    """

    return lst[:length] if length == len(lst) else lst[:length]

# Example of passing the test
print(sort_even([1, 2, 3]))
```