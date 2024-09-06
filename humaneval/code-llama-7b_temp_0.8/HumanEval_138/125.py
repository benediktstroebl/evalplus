
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    sum = 0
    for i in range(0, 4):
        for j in range(0, 4):
            if j != i:
                for k in range(0, 4):
                    if k != j and k != i:
                        for l in range(0, 4):
                            if l != k and l != j and l != i:
                                if i + j + k + l == n:
                                    return True
    return False
