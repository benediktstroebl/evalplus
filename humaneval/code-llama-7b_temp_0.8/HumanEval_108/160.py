
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
    # #code 1
    # ans = 0
    # for i in arr:
    #     if sum(list(map(int, str(i)))) > 0:
    #         ans += 1
    # return ans

    # #code 2
    # return len(list(filter(lambda x: sum(list(map(int, str(x)))) > 0, arr)))

    # code 3
    return sum(sum(list(map(int, str(i)))) > 0 for i in arr)
