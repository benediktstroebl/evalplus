
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    n = int(n)
    if n < 2 or n % 2 != 0:
        return False
    if n % 4 == 0:
        return False
    sum = 0
    for i in range(3, n + 1, 2):
        sum += i
    if sum % 2 == 0:
        return False
    return True