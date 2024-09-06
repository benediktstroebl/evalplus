
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    even = []
    if n % 2 == 0:
        even.append(n)
    else:
        return False
    for i in range(2, int((n / 2) + 1)):
        if n - i in even:
            return True
    return False

