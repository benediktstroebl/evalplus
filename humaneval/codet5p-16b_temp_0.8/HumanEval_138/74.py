
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    a, b, c, d = 0, 0, 0, 0
    while a <= n:
        if a % 2 == 0:
            b += a
        else:
            a += 1
    while b <= n:
        if b % 2 == 0:
            c += b
        else:
            b += 1
    while c <= n:
        if c % 2 == 0:
            d += c
        else:
            c += 1
    return d == n
