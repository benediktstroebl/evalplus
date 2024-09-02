
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
    def find_sum_of_digits(num):
        return sum([int(i) for i in str(num)])

    # input should be a list of integers
    return sum([True if find_sum_of_digits(i) > 0 else False for i in arr])
