
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

    def sum_digits(num):
        if num < 0:
            first_digit = -1 * (int(str(num)[0]))
            other_digits = int(str(num)[1:])
            return first_digit + sum_digits(other_digits)
        return sum(int(digit) for digit in str(num))

    return len([num for num in arr if sum_digits(num) > 0])

    # TODO: remove when the solution is complete
    return 0
