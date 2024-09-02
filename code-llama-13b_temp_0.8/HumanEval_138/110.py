
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 == 1:
        return False
    if n == 0:
        return False
    n = n//2
    i = 1
    while i <= n:
        j = 1
        while j <= n:
            k = 1
            while k <= n:
                l = 1
                while l <= n:
                    if i + j + k + l == n:
                        return True
                    l += 1
                k += 1
            j += 1
        i += 1
    return False

