
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    for a in range(2, n):
        for b in range(2, n):
            for c in range(2, n):
                for d in range(2, n):
                    if a+b+c+d == n:
                        return (a%2 == 0) and (b%2 == 0) and (c%2 == 0) and (d%2 == 0)
    return False



