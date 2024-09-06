
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    if n < 8:
        return False

    if n % 2 == 1:
        return False

    result = False
    i = 2
    while i <= (n / 2):
        j = i + 2
        while j <= (n / 2):
            if i != j:
                k = i + j
                if k >= n:
                    break
                l = n - i - j
                if k == l:
                    result = True
                    break
            j += 2
        if result == True:
            break
        i += 2

    return result

