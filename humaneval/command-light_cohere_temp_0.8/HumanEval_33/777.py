```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 20, 30, 40, 50, 80, 100, 70])
    [80, 100, 70, 50, 40, 30, 20, 10]
    """
    l1 = []
    for i in l:
        if (i % 3 == 0) or ((i % 3) == 1):
            l1.append(i)
   
    l.append(i)
   
    return l1
```  This function will take a list and will create a new list that will have the elements that are divisible by three as they are the same in the original list, and all other elements will be sorted in ascending order.