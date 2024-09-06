```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the
    indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 15, 3, 16, 4, 5])
    [2, 3, 15, 16, 4, 5, 10]
    """
    # initialize a new list to store sorted third-digits
    l_3rd = [0 for i in l]

    # loop through original list and add corresponding third-digit value to l_3rd
    for i, num in enumerate(l):
        if num % 3 == 0:
            l_3rd[i] = num
    # loop through original list and add first element to l'
    for i, num in enumerate(l):
        l_3rd[i] = num + l_3rd[i - 1]
    return l_3rd
```