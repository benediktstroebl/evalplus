
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    x = 2
    for i in range(2, 9):
        for j in range(2, 9):
            for k in range(2, 9):
                for m in range(2, 9):
                    if i + j + k + m == n and i % 2 == 0 and j % 2 == 0 and k % 2 == 0 and m % 2 == 0:
                        return True
    return False
