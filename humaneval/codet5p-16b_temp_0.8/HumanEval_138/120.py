
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    n = str(n)
    n_sum = 0
    for i in range(len(n)):
        n_sum += int(n[i])
    if n_sum % 2 == 0:
        return True
    return False
