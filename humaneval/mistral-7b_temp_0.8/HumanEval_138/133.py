
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 4 != 0:
        return False
    numbers = []
    while len(numbers) < 4:
        n -= 2
        if n < 0:
            return False
        if numbers.count(n) > 0:
            return False
        numbers.append(n)
    return True

