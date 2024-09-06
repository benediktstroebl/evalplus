```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the 
    indicies that are not divisible by three, while its values at the indicias that are divisible 
    by three are equal to the values of the corresponding indicias of l, but sorted. """

    same: List"""
    l_ = [1, 2, 3]
    l_ = sorted([x for x in l if x % 3 == 0], reverse = True)
    l_ = [x if x != 3 else x[-1] for x in l_ ]
    l = list(l_)
    return l
```