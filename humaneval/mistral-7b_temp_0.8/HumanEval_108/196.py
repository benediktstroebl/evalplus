
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

    # --- Your code here ---
    # count = 0
    # for i in arr:
    #     if sum([int(x) for x in str(i)]) > 0:
    #         count += 1
    # return count
    #

    # for num in arr:
    #     count = 0
    #     for x in str(num):
    #         count += int(x)
    #     if count > 0:
    #         print(count)

    # if arr == []:
    #     return 0
    # else:
    #     return sum(arr)

    # for i in arr:
    #     if i > 0:
    #         print(i)

    count = 0
    for i in arr:
        if sum([int(x) for x in str(i)]) > 0:
            count += 1
    return count

