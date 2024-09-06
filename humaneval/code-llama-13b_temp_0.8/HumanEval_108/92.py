
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

    def has_positive_digit_sum(num):
        """Takes a number and returns whether its digits sum to > 0."""
        sum = 0
        while num != 0:
            sum += num % 10
            num = num // 10
        return sum > 0

    return len([num for num in arr if has_positive_digit_sum(num)])

