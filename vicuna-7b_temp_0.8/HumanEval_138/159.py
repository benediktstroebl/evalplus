
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Using a recursive function
    def is_equal_to_sum_even_helper(n, sum_even, remainder):
        if n == 0:
            return True
        elif n % 2 == 0:
            return is_equal_to_sum_even_helper(n//2, sum_even + (n//2), remainder)
        else:
            return is_equal_to_sum_even_helper(n, sum_even, (n+1) // 2)

    sum_even = 0
    remainder = 1
    return is_equal_to_sum_even_helper(n, sum_even, remainder)
