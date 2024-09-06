
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
    "*** YOUR CODE HERE ***"
    count = 0
    for i in arr:
        if i >= 0:
            d = i
        else:
            d = abs(i)
        while d != 0:
            d = d // 10
            count += 1
    return count
