
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n%2 == 1:
        return False
    if n % 4 == 0:
        return True
    if n % 6 == 0:
        return True
    if n % 8 == 0:
        return True
    if n % 10 == 0:
        return True
    if n % 12 == 0:
        return True
    if n % 14 == 0:
        return True
    if n % 16 == 0:
        return True
    if n % 18 == 0:
        return True
    if n % 20 == 0:
        return True
    if n % 22 == 0:
        return True
    if n % 24 == 0:
        return True
    if n % 26 == 0:
        return True
    if n % 28 == 0:
        return True
    if n % 30 == 0:
        return True
    if n % 32 == 0:
        return True
    if n % 
