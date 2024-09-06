
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 == 0 and n > 4:
        a = [2, 4, 6, 8]
        b = [2, 4, 6, 8]
        c = [4, 6, 8]
        d = [6, 8]
        if n in a:
            return True
        elif n in b:
            return True
        elif n in c:
            return True
        elif n in d:
            return True
    else:
        return False
