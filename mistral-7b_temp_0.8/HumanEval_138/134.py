
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    number = n
    even = 0
    while number > 0:
        if number % 2 == 0:
            even += 1
        number //= 2
    return even == 4
