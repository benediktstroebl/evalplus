
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n == 0:
        return False

    i = 1
    while i <= (n / 2):
        j = 1
        while j <= (n / 2):
            k = 1
            while k <= (n / 2):
                t = 1
                while t <= (n / 2):
                    if i + j + k + t == n:
                        return True
                    t = t + 2
                k = k + 2
            j = j + 2
        i = i + 2

    return False
