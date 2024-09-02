
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    numbers_to_check = range(2, n)
    numbers_sum = 0
    for number in numbers_to_check:
        if number % 2 == 0:
            numbers_sum += number
    if numbers_sum == n:
        return True
    return False
