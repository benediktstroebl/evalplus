
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 4:
        return False

    def is_even(n):
        return n % 2 == 0

    if not is_even(n):
        return False

    def is_n_times_even(n, even_number_count):
        return even_number_count * 2 == n

    return is_n_times_even(n / 2, 2)

