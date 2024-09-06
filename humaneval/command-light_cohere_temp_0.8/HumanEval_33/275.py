```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l
    in the items that are not divisible by three, while its values at positions that are divisible by three are
    equal to the values of the corresponding positions of l, but sorted.
    """Note that this list is passed by value, so you must use list comprehensions to create sublists for passing to the function.
    """Example usage:
    >>> sorted_third([1, 2, 3])
    [1, 2, 3]
    >>> sorted_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    return sorted(l, key=lambda x: not_divisible(x,3), reverse=True)

def not_divisible(x, n):
    return x // n == 0
```
The function `sort_third` sorts a list l such that each value at a position x that is divisible by three is replaced with the value of the corresponding position of l, but the values at positions x that are not divisible by three are left unmodified. The function `not_divisible` checks whether x is divisible by n, and returns True if it is, False otherwise.