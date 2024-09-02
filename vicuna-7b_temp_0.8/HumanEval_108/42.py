
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
    arr = list(arr)
    arr.sort()
    count = 0
    for num in arr:
        if num > 0:
            count += 1
    return count

@with_setup(setup={"arr": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
