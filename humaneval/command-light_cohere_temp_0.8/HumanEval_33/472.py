```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 30, 40, 50, 60, 20, 70])
    [10, 20, 30, 40, 50, 60, 70]
    """
    return sorted(lst, key=lambda x:int(x) // 3 if x.is_divisible(3) else x)
```
The function takes a list `lst` as input and returns a sorted list `lst_sorted`. The function uses the `sorted()` function along with a lambda function as the key argument in the `sorted()` function. The lambda function identifies the specific items in the list that are divisible by 3, such as 3, 6, 9, and so on.