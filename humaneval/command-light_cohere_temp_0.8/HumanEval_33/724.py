```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
    
    :param l: list
    l.return equals_values for indices that are divisible by three
    """
    l.sort(key=lambda x: not (x%3 == 0))
    l = [x for x in l if not (x%3 == 0)]
    l.sort(key=lambda x: x%3 == 0)
    l.sort()
    value=l, 
    return l
```