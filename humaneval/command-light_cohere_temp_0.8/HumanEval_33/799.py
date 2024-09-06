```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([11, 22, 33, 55, 8, 18, 99])
    [99, 55, 33, 22, 18, 11]
    """
    l_prime = []
    for i in l:
        if i % 3 != 0:
            l_prime.append(i)
   
    l_prime.append(l[i])
    l = l_prime
    return l
```