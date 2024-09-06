```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the 
    indicies that are not divisible by three, while its values at the indicies numbers that are divisible by three are equal to the values of the corresponding 
    indic of l, but sorted.
    """
    list l' return the list l' sorted by the values of l except those that are divisible by three.
    """
list l = [5, 6, 3, 4, 8, 9, 2]
    l = sort_third(l)
    assert l == [2, 6, 3, 4, 8, 9, 5]
```