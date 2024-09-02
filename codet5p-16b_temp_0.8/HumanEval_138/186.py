
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    n = abs(n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if i + j + k + l == n:
                        return True
    return False

