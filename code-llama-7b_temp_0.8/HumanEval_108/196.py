
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
    def signed_digits(n):
        digits = []
        if n < 0:
            digits.append(-1)
        while n > 0:
            n, digit = divmod(n, 10)
            digits.append(digit)
        return digits
    
    def num_has_positive_digit(n):
        for d in signed_digits(n):
            if d > 0:
                return True
        return False
    
    num_of_positive_digits = 0
    for num in arr:
        if num_has_positive_digit(num):
            num_of_positive_digits += 1
    return num_of_positive_digits

