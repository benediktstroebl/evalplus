```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the odd indic, while its values at the even indices are equal to the values of the even indicies of l, but sorted."""
    new_list = []
    for num in l:
        if num % 2 == 0:
            new_list.append(num)
   
    return new_list
```