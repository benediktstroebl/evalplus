
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
    # count = 0
    # for i in arr:
    #     a = str(i)
    #     if len(a) > 0:
    #         if sum([int(i) for i in a]) > 0:
    #             count += 1
    # return count
    return sum(1 for i in arr if sum([int(i) for i in str(i)]) > 0)
