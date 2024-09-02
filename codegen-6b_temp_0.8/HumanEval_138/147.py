
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2:
        return False
    if n < 4:
        return False

    nb_divisors = 4
    for i in xrange(n / 2, 1, -2):
        if n % i:
            nb_divisors += 1
        else:
            nb_divisors -= 1
            if nb_divisors < 0:
                return False
    return True
