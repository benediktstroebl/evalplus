```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted."""
    l_sorted = []
    for num in l:
        if(num%3 == 0):
            l_sorted.append(num)
        else:
            l_sorted.append(num) 
    return(l_sorted)
```