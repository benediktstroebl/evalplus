
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    if n == 0:
        return True
    if n % 2!= 0:
        return False
    if n <= 4:
        return True
    numbers = [2, 4, 6, 8]
    number_sum = 0
    for number in numbers:
        if n > number:
            n -= number
            number_sum += number
    return is_equal_to_sum_even(n)

