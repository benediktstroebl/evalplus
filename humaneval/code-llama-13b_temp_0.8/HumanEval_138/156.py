
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n == 0:
        return False
    i = 0
    while i <= n:
        j = 0
        while j <= n:
            k = 0
            while k <= n:
                m = 0
                while m <= n:
                    if i + j + k + m == n:
                        if i % 2 == 0 and j % 2 == 0 and k % 2 == 0 and m % 2 == 0:
                            return True

                    m += 1
                k += 1
            j += 1
        i += 1

    return False

