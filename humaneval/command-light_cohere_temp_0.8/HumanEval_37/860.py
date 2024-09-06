```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indic, while its values at the even index are equal to the values of the even indic of l, but sorted.

    :param list l:
    l: list to be sorted
    """
    # identify even index
    even = [i for i, x in enumerate(l) if x % 2 == 0]

    # sort the even index to the back
    l = [x if i in even else y for i, x in enumerate(l)] + l[even]

    return l

# test cases
print(sort_even([1, 2, 3]))   
# Expected Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  
# Expected Output: [3, 6, 5, 4]
```