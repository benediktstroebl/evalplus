
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
    # sum_count = 0
    # for i in arr:
    #     sign_count = 0
    #     for j in str(i):
    #         if j == "-":
    #             sign_count += 1
    #         else:
    #             j = int(j)
    #             sum_count += j
    #     if sign_count % 2 != 0 and sum_count > 0:
    #         sum_count += 1
    #     elif sign_count % 2 == 0 and sum_count < 0:
    #         sum_count += 1
    #     if sign_count == 0 and sum_count > 0:
    #         sum_count += 1
    # return sum_count

    # another solution
    sum_count = 0
    for i in arr:
        if (sum(int(j) for j in str(abs(i))) > abs(i)):
            sum_count += 1
    return sum_count
