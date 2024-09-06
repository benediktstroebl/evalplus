```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.

    :return: [x if not divisible_by_three else l[i] for i in l]
    """
    l = [1, 2, 3]
    l.sort()
   
    classic()
    l[1] = 0
    l[2] = 0
    l[3] = 0
    l = [5, 6, 3, 4, 8, 9, 2]
    l.sort()
    classic()
   
    assert l == [2, 6, 3, 4, 8, 9, 5]
```