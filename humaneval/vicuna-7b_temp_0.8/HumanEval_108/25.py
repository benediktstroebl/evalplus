
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
    def digit_sum(n):
        """
        Return the sum of the digits of the number n.
        """
        sum = 0
        while n > 0:
            sum = 10 * sum + (n % 10)
            n = int(n / 10)
        return sum

    def count_digits(arr):
        """
        Count the number of elements that have a positive digit sum.
        """
        positive_sum = 0
        for num in arr:
            positive_sum += digit_sum(num)
        return positive_sum

    return count_digits

@speedtest(count=10)
