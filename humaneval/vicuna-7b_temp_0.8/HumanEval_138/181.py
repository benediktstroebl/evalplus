
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    sum_even = 0
    for i in range(n):
        if (n % 2) == 0:
            sum_even += n // 2
        else:
            sum_even += n
    return sum_even == n

