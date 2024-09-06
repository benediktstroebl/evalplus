```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the 
    indicies that are not divisible by three, while its values at the indicatives that are divisible 
    by three are equal to the values of the corresponding indicatives of l, but sorted.
    """
    list comprehension and and sorting by the remainder of the gcd with 3.
    """
    list l' values with a gcd of 3."""
    l[:] = [x for x in l if x % 3 == 0] + [x for x in l if x % 3 != 0]
    return list(sorted(l,key=lambda x: math.gcd(x,x)%3))
```