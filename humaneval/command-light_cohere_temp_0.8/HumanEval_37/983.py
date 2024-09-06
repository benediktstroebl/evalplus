```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted.
    >>> sorted( [1, 2, 3])
    [1, 2, 3]
    >>> sorted([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([4, 8, 10, 12])
    [8, 10, 12, 4]
    >>> sort_even([1, 2, 3, 4, 5])
    [1, 2, 3, 4]
    """
    l.append(4)  #create a new even element at the end of the list
    l.sort_even()
   
    #sort the even elements
    return l[:] #return the first half of the sorted list

```