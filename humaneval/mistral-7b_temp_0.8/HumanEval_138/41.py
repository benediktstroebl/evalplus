
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    for i in range(1, int(n**(0.5))+1):
        if n % i == 0:
            if i % 2 == 0:
                if is_equal_to_sum_even(n-i):
                    return True
            else:
                if is_equal_to_sum_even(n-i):
                    return True

    return False

