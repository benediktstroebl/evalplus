```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the index that are not divisible by three, while its values at the index that are divisible by three are equal to the values of the corresponding index of l, but sorted.
    Args:
    l: list
    Returns: l' which passes the test
    """
    new_lst = []
    for ind, val in enumerate(lst):
        if val % 3 != 0:
            new_lst.append(val)
   
    return new_lst

# Example usage
my_list = [5, 6, 3, 4, 8, 9, 2]
print(sort_third(my_list))
```