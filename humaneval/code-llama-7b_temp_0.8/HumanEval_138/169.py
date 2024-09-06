
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 6 or n % 2 == 1:
        return False
    n_str = str(n)
    for i in range(int(n_str[0]), int(n_str[1])):
        for j in range(int(n_str[2]), int(n_str[3])):
            if (i + j) == n:
                return True
    return False
