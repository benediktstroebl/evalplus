
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
    def check(num):
        if not (0 <= num <= 9):
            return 0
        if num in [1, 11, 10]:
            return 1
        for i in range(num):
            if (num-i) in [1, 11, 10]:
                return check(num-i) + 1
        return 0
    return len(filter(lambda x: check(x), arr))