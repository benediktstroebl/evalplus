
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    n = int(n)
    if n % 2 == 1:
        return False
    else:
        result = 0
        while (n > 0):
            digit = n % 10
            result += digit
            n = n // 10
        if result % 2 == 0:
            return True
        else:
            return False

