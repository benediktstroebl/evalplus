```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted.

    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> sort_even([10, 11, 12])
    Traceback (most recent call last):
      File "<stdin>", line 7, in sort_even()
      File "<string>", line 3, in <module>
        raise ValueError('Input list must be a list of integers')
    ValueError: Input list must be a list of integers
  ```
The function `sort_even` takes a list `l` as input and returns a list `l'` with elements from odd indexes and even indexes of the original list, and elements are sorted as equal to their corresponding even index values.