```python
def sort_third(lst):
    """This function sorts a list l such that the values at indices that are not divisible by three are in their original order, while the values at indices that are divisible by three are sorted alphabetically.

    : Raises ValueError if the accomplished.

    """ Return input list l, a list or tuple of numbers"""
    if type(lst) is not list:
        raise ValueError("Input must be a list")
    if all(isinstance(num, int) and num % 3 == 0 for num in l):
        return lst[:]
    else:
        lst[:] = sorted(lst, key=lambda num:num//3 if num%3 else num)
    return lst
``` 
Here, the function sorts the list such that the values at indices that are not divisible by three are in their original order, while the values at indices that are divisible by three are sorted alphabetically. If the input is not a list or if any of the elements are not integers or if any element is not divisible by three, the function raises a ValueError.