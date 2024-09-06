```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the odd indic, while its values at the even indicies are equal to the values of the even indic of l, but sorted."""
    l = [1, 2, 3]
    l.sort_even(l)
    assert l == [1, 2, 3] #First test 
    l = [5, 6, 3, 4]
    l.sort_even(l)
    assert l == [3, 6, 5, 4] #Second test 
    l = [9, 8, 7, 10]
    l.sort_even(l)
    assert l == [7, 8, 9, 10] #Third test 
```