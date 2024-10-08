
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    total = 0
    x = 1
    while x <= n / 2:
        if is_prime(x) and n - x in nums:
            total += x
            total += n - x
            x += 2
        else:
            x += 1
    return total == n
