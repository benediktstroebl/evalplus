
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # return 4 in range(n+1) and all([i for i in range(n+1) if i % 2 == 0][1:-1])
    return n > 3 and all([i for i in range(n+1) if i % 2 == 0][1:-1])
