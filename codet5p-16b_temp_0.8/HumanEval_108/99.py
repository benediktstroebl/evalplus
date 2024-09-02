
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """

    
    if not arr:
        return 0
    return count_nums([el for el in arr if sum([int(x) for x in str(el)]) > 0]) + len([el for el in arr if sum([int(x) for x in str(el)]) == 0])
