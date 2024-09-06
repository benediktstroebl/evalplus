
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    if n%2 != 0:
        return False

    if n <= 0:
        return False

    if n == 2:
        return True

    if n <= 6:
        return False

    if n >= 8:
        return True

    i = 1
    total = 0
    while i <= (n/2):
        if i%2 == 0:
            total += i
        i += 1
    if n == total:
        return True
    else:
        return False
