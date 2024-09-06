```python
def sort_third(lst):
    """This function sorts a list l according to the rule that numbers not divisible by three come first, and numbers divisible by three are left as they are.
    The list is sorted so that the first element is a number not divisible by three,
    the second is a number divisible by three, and so on.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 3, 4, 5, 6, 7])
    [10, 7, 6, 5, 3, 4]
    >>> sort_third([9, 8, 7, 6, 5, 4, 3])
    [4, 5, 3, 6, 7, 8, 9]
    """
    return sorted(lst, key=lambda x: not_divisible(x))

def not_divisible(x):
    """This function returns True if x is divisible by three, False otherwise.
    return True if x% of x is divisible by 3 and the remainder is 0, False otherwise
    """
    return x % 3 == 0
```