```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 13, 45, 67, 19])
    Traceback (most recent call last):
      File "<string>", line 7: raise or assert statement failed:
      File "<string>", line 4: 0 is not divisible by 3
    AssertionError: list index (10) is out of range
    """

# Your code here
```