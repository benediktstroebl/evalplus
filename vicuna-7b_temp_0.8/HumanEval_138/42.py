
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 0 or n > 10000:
        return False
    if n % 2 == 0:
        return True
    sum_even = 0
    for i in range(2, n + 1):
        if (n % i) == 0:
            sum_even += i
    return n == sum_even
