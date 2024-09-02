
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
    def count_digits(num):
        """
        Given an integer num, return a list of its digits in reverse order.
        """
        digits = []
        while num > 0:
            digits.append(num % 10)
            num = divmod(num, 10)[0]
        digits.reverse()
        return digits
    
    def sum_digits(arr):
        """
        Given an array of integers, return the number of elements which have a
        sum of digits > 0.
        """
        return len(filter(lambda x: sum(count_digits(x)['0']) > 0, arr))
    
    return sum_digits