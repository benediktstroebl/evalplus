
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
    assert not isinstance(arr, int), 'arr should be array, not int'
    assert all([isinstance(i, int) for i in arr]), 'arr should contain only ints'

    def get_digit(i):
        if i < 0:
            return - (abs(i) % 10)
        else:
            return i % 10

    def get_sum_of_digits(i):
        if i == 0:
            return 0
        else:
            return get_digit(i) + get_sum_of_digits(i // 10)

    return sum([get_sum_of_digits(i) > 0 for i in arr])
