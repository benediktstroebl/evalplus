```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 3, 5, 6, 7, 8, 9])
    [10, 3, 5, 6, 7, 8, 9, 2]
    >>> sort_third([1, 2, 3, 4, 5, 6, 7, 8, 9])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    lst = list(map(lambda x: x if x % 3 == 0 else x +1, l))
    lst.sort()
    yet (lambda x: x)
``` 
This script defines a function `sort_third` that takes a list `lst` as an argument. It creates a map function that adds 1 to the elements that are divisible by 3 and leaves the other elements unchanged. Then, it uses the sort function to sort the resulting list. The test cases demonstrate the different expected results.