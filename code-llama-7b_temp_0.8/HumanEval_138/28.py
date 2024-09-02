
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    for i in range(1, n):
        for j in range(1, i):
            for k in range(1, j):
                for l in range(1, k):
                    if i + j + k + l == n:
                        return True
    return False

