```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 13, 22, 11, 15, 33, 19, 80])
    [33, 22, 19, 15, 11, 10, 13, 80, 22, 6]
    >>> sort_third([90, 80, 50, 25, 30, 19, 120])
    [19, 30, 50, 80, 90, 120]
    """
    # implement your sorting logic here
    l1 = [10, 2, 13, 22, 11, 15, 33, 19, 80]
    l2 = [90, 80, 50, 25, 30, 19, 120]
    return [x if x not divisible(3) else x[0] for x in l] + [x if x divisible(3) else x[1] for x in l]
```
The function uses a built-in Python function `divisible()` that checks if a number is divisible by another number. The function then performs two separate passes on the list: first, it removes values that are divisible by three and instead replaces them with the value at the corresponding index of the original list, and second, it removes values that are not divisible by three and instead replaces them with the first value from the original list.