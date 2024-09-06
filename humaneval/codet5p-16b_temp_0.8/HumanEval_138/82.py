
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    n = str(n)
    even_sum = 0
    for i, n in enumerate(n):
        even_sum += int(n) if i % 2 == 0 else 0
    if even_sum == 4:
        return True
    return False
