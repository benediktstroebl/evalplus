
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

    # WRITE YOUR CODE HERE
    num = [abs(i) for i in arr]
    sum_num = [sum([int(x) for x in str(i)]) for i in num]
    return sum([1 for i in sum_num if i > 0])
