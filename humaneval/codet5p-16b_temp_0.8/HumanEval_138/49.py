
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    numbers = [1, 2, 3, 4]
    if n % 2!= 0:
        return False
    numbers_in_range = list(filter(lambda x: x <= n / 2, numbers))
    if len(numbers_in_range) < 4:
        return False
    if len(numbers_in_range) == 4:
        return sum(numbers_in_range) == n
    else:
        return sum(numbers_in_range[0:4]) == n
