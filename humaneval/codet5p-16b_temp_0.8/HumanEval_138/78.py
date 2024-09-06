
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    even_numbers = [x for x in range(2, n) if x % 2 == 0]
    if len(even_numbers) > 3:
        return False
    for i in even_numbers:
        if n - i not in even_numbers:
            return False
    return True
