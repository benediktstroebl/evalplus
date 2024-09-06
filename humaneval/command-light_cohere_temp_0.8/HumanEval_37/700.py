```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([10, 20, 30, 40])
    [10, 20, 30, 40]
    """
    l1 = [1, 2, 3]
    l2 = [5, 6, 3, 4]
    l3 = [10, 20, 30, 40]
    
    even_index = len(l)//2
    l1 = l1[:even_index] + l1[even_index+1:]
    l2 = l2[:even_index] + l2[even_index+1:]
    l3 = l3[:even_index] + l3[even_index+1:]
    
    l = [x for x in l3 if x in l1] + l1 + l2 + l3[::-1]
    return l
```