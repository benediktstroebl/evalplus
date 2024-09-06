```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 15, 6, 18, 9])
    [2, 6, 15, 18, 9]
    >>> sort_third([5, 6, 3, 9, 9, 4, 3, 6, 5])
    [3, 6, 5, 4, 9, 3, 6, 5]
    """
    # create list with values divisible by 3
    divisible = [3, 6, 9]
    # create list with values not divisible by 3
    notDivisible = [1, 2, 5, 8, 10, 15, 18]
    # combine both lists into a new list
    list_temp = list(divisible) + list(notDivisible)
    # sort list_temp by value, so divisible comes first
    list_temp.sort_by_value()
   
    # convert list_temp back to a list
    return list_temp
```