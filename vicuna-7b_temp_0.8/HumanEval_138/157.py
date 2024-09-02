
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n <= 4:
        return True
    if n % 2 == 0:
        return False
    n_even = 0
    for i in range(3, n+1, 2):
        n_even += i
    if n == n_even:
        return True
    return False