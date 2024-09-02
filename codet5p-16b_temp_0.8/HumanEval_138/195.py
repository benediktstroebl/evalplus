
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    result = False
    for i in range(1, n):
        for j in range(2, n):
            for k in range(3, n):
                for l in range(4, n):
                    if i + j + k + l == n:
                        result = True
    return result

