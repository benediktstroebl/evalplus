
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    assert type(n) == int, 'The input n should be an integer'
    assert n > 0, 'The input n should be positive'

    number = n
    is_multiple_of_4 = False
    for i in range(2, number):
        if number % i == 0 and number % 2 == 0:
            is_multiple_of_4 = True
            break

    return is_multiple_of_4

