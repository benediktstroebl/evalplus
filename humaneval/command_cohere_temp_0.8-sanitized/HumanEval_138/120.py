def is_equal_to_sum_even(n):
    """
    Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    :param n: Number to be evaluated
    :return: True if the number can be expressed as sum of 4 positive even numbers, otherwise False
    """
    if n <= 0:
        return False
    
    # Ensure n is even to simplify the problem
    if n % 2 == 1:
        return False
    
    # Generate all combinations of 4 even numbers (2, 4, 6, 8) and sum them
    even_combos = [2, 4, 6, 8]
    return any(sum(even_combo) == n for even_combo in even_combos)