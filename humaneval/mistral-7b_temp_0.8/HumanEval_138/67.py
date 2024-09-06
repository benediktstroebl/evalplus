
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # your code here
    if n % 4 != 0:
        return False
    if n <= 4:
        return False
    sum_of_2 = 2 * n / 4
    if sum_of_2 != int(sum_of_2):
        return False
    return True
