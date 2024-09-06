```python
def sort_even(lst):
    """This function takes a list l and returns a list l' such that l' is identical to l in the odd indic, while its values at the even indicies are equal to the values of the even indic of l, but sorted."""
    even, odd = divmod(len(lst), 2)
    lst[:even] = lst[even::2] + [even] * (len(lst) - even)
    return lst

# Test the function
# Perform the test in a markdown code block
```python
>>> sort_even([1, 2, 3])
[1, 2, 3]
>>> sort_even([5, 6, 3, 4])
[3, 6, 5, 4]
```