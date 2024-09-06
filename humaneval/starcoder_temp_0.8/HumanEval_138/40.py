
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    for a in range(4, n):
        if a % 2 == 0:
            for b in range(4, n):
                if b % 2 == 0:
                    for c in range(4, n):
                        if c % 2 == 0:
                            for d in range(4, n):
                                if d % 2 == 0:
                                    if a + b + c + d == n:
                                        return True
    return False
