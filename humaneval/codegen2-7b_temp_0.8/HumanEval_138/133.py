
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    def is_pos_even(n):
        return n % 2 == 0 and n >= 0

    if is_pos_even(n) and n > 0:
        for i in range(1, n):
            if is_pos_even(i * (n - i) // 2) and i * (n - i) // 2 > 0:
                return True

    return
