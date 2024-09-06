```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    def third_divisible(n):
        return n % 3 == 0

    l = [1, 2, 3]
    l = [n for n in l if third_divisible(n)]
    l.sort()
    also works:
    [1, 2, 3]
    [2, 6, 3, 4, 8, 9, 5]
    [2, 6, 3, 4, 8, 9, 5]
    ```