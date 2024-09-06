```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 13, 20, 21,11, 15])
    [10, 11, 13, 20, 21, 15, 2]
    """
    l=list(range(0,int(l[0])+1))
    for i in range(1,len(l)):
        if l[i]%3==0:
            l[i],l[i-1]=l[i-1],l[i]
    else: pass
    return l
```