
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    if n % 2!= 0: # if the given number is not even, it can't be written as the sum of exactly 4 positive even numbers
        return False

    evens = [2, 4, 6, 8]
    for a in evens:
        for b in evens:
            if a + b == n:
                return True

    return False
