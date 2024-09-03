```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted."""
    return l[:len(l)//2] + [x for x in l[len(l)//2:]];
``` 
This function uses list slicing and list comprehension to achieve the desired sorting.