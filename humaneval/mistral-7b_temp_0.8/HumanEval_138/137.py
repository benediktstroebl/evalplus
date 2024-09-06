
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    for i in range(2, n//2+1):
        for j in range(i, n//2+1):
            if (i + j)%2 == 0:
                sum = i + j
                if n - sum == 0:
                    return True
                elif n - sum > 0:
                    return False
                elif n - sum < 0:
                    pass

    return False

