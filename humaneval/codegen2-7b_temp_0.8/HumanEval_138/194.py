
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    sum_of_even = sum(filter(lambda x: x % 2 == 0, range(1, n+1)))
    return sum_of_even == n and n % 2 == 0

