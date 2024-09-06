
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
    # my solution
    def sum_digits(num):
        s = 0
        while num > 0:
            s += num % 10
            num //= 10
        return s

    def number_digits(num):
        s = 0
        while num > 0:
            num //= 10
            s += 1
        return s

    def count_pos(lst):
        if len(lst) == 0:
            return 0
        elif sum_digits(lst[0]) > 0:
            return count_pos(lst[1:]) + 1
        else:
            return count_pos(lst[1:])

    return count_pos(arr)

