
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 8:
        return False
    if n % 2 != 0:
        return False
    for i in range(4):
        for j in range(i+1, 4):
            for k in range(j+1, 4):
                for l in range(k+1, 4):
                    if n == (2*i + 2*j + 2*k + 2*l):
                        return True
    return False

