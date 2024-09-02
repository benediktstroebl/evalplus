
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    i = 1
    count = 0
    if n % 2 == 0:
        return False
    else:
        while i <= n:
            if n - i % 2 == 0:
                count += 1
                if count == 4:
                    return True
                else:
                    i += 1
                    continue
            else:
                i += 1
                continue
        return False

