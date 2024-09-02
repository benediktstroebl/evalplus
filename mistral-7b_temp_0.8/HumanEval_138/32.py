
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    from math import sqrt
    # check if n is square of an even number
    square = sqrt(n)
    if square.is_integer() and square % 2 == 0:
        return True
    # check if n is a sum of 2 even numbers
    for i in range(1, n):
        if n - i in [2 * j for j in range(2, n - i)]:
            return True
    return False
