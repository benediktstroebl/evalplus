
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n == 4 or n == 6 or n == 8:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if n // i != i:
                return False
            break
    return True
