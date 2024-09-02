
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    a = 2
    b = 4
    c = 6
    d = 8
    while a <= n:
        while b <= n:
            while c <= n:
                while d <= n:
                    if a + b + c + d == n:
                        return True
                    d += 2
                c += 2
            b += 2
        a += 2
    return False
