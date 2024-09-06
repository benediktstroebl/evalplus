
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    if n%2 == 1:
        return False
    else:
        n = int(n)
        sum = 0
        while n > 0:
            if n%2 == 0:
                sum += n
                n -= 1
            else:
                n -= 1
        if sum%2 == 0:
            return True
        else:
            return False

