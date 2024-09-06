
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
    # Use the map and reduce functions to create the sum_of_digits function
    # which takes an integer and returns the sum of its digits.
    # Use sum_of_digits to check if the number's sum_of_digits > 0.

    def sum_of_digits(num):
        return sum([int(digit) for digit in str(num)])

    return sum(num > 0 for num in map(sum_of_digits, arr))

