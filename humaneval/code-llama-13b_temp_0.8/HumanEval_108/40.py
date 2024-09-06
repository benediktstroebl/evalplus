
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
    # t = 0
    # for i in arr:
    #     s = str(i)
    #     if i >= 0:
    #         s = str(i)
    #     else:
    #         s = str(i)[1:]
    #         s = '-' + s
    #     t += sum(int(c) for c in s)
    # return t

    return len(list(filter(lambda x: sum(int(c) for c in str(x)) > 0, arr)))
