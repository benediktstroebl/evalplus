
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    n_str = str(n)
    if len(n_str) < 4:
        return False
    return sum(int(n_str[x]) for x in range(0, 4) if n_str[x] == '2' and int(n_str[x]) % 2 == 0) == 0

