
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
    # count_nums([-1, 11, -11]) == 1
    # count_nums([1, 1, 2]) == 3
    # count_nums([1, 1, -2]) == 2
    # count_nums([-1, 11, 11, 1]) == 3

    # r = []
    # for i in arr:
    #     r.append(digits_sum(i))
    # return r.count(True)
    return sum([1 if digits_sum(i) > 0 else 0 for i in arr])
