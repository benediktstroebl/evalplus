
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n%2 != 0:
        return False
    else:
        i = 1
        j = 1
        s = 0
        while True:
            if s == n:
                return True
            if s > n:
                break
            s = i + j
            j += 2
            i += 2
        return False
