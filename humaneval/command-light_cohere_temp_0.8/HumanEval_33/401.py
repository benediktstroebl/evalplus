```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the items that are not divisible by three, while its values at the items divisible by three are equal to the values of the corresponding items of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([11, 22, 33, 99, 88, 22, 11, 99])
    [11, 22, 33, 99, 88, 22, 11]
    """
    l1 = []
    for num in l:
        if num % 3 == 0:
            l1.append(num)
   
    l = l1
    l.sort()
    done using
    done! done
```