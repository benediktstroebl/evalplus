
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    """
    At first we check that the number of even numbers in the list is less than 4.
    If so, we go through the list and for each even number we check if its complement is in the list
    and if so then we add it to the sum and if the sum equals 4, we return True.
    """
    if n % 2 != 0 or len(list(filter(lambda x: x % 2 == 0, list(range(1, n // 2)))) - len(filter(lambda x: x == n - x, list(range(1, n // 2)))) + 1) < 4:
        return False
    else:
        return True

