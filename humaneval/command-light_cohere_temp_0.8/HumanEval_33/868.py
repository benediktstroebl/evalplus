```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    Args:
    l (list): list to be sorted with respect to third divisor.
    Returns: list l'
   
    """
    l = [5, 6, 3, 4, 8, 9, 2]
    l.sort_third()  # , 3, -1
    return l 
```