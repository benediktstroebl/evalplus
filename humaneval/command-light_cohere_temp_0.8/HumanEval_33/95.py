```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
    
    :type lst: list = l[:]
    n = len(lst)
    #find the indices of the values that are divisible by three
    i = 0
    while(i < n):
        if(l[i]%3 == 0):
            i += 1
        else:
            lst.insert(0, l[i])
            i += 1
    l = lst
    return l
```