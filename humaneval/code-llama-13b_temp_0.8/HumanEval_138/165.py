
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    if n < 8:
        return False
    elif n % 2 != 0:
        return False

    a = 1
    while a <= n - a:
        b = a + 1
        while b <= n - a - b:
            c = b + 1
            while c <= n - a - b - c:
                d = c + 1
                while d <= n - a - b - c - d:
                    if a + b + c + d == n:
                        return True
                    d += 1
                c += 1
            b += 1
        a += 1
    return False

