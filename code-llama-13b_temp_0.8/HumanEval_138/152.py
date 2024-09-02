
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    if n % 2 != 0:
        return False
    elif n == 0:
        return False
    else:
        i = 2
        while i <= n/4:
            j = i + 1
            while j <= n/2:
                if n == i + j + i + j:
                    return True
                j += 1
            i += 1
        return False

    return n % 4 == 0 and n != 0


