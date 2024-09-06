
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    if (n % 4)!= 0:
        return False
    even_numbers = [2, 4, 6, 8]
    n_divisors = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            n_divisors += 1
    if n_divisors == 4:
        return True
    else:
        return False

