
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    even_sum = 0
    n_even = n
    i = 2
    while n_even > 0:
        even_sum += n_even % i
        n_even = n_even // i
    if even_sum == n:
        return True
    return False
