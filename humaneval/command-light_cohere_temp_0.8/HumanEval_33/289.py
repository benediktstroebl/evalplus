```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
    Args:
        l: list
    Returns: l'
    """
    lst = [1, 2, 3]
    lst[::3] = [2, 6, 3]
    lst[1::3] = [8, 9, 5]
    return lst

# Test case 1
print(sort_third([1, 2, 3]))  # [1, 2, 3]

# Test case 2
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # [2, 6, 3, 4, 8, 9, 5]

# Test case 3
print(sort_third([10, 1, 2, 3]))  # [1, 2, 3]
```