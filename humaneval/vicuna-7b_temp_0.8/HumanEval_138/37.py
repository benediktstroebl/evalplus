
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    n = int(n)
    if n < 4 or not any(n % i == 0 for i in range(1, n + 1)):
        return False
    sum_of_even = sum(range(1, n + 1))
    if n == sum_of_even:
        return True
    return False
