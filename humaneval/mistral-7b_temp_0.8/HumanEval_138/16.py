
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    a = n
    b = n
    c = n
    d = n
    while a > 2:
        if a % 2 == 0:
            a = a // 2
        else:
            a = a - 1
    while b > 2:
        if b % 2 == 0:
            b = b // 2
        else:
            b = b - 1
    while c > 2:
        if c % 2 == 0:
            c = c // 2
        else:
            c = c - 1
    while d > 2:
        if d % 2 == 0:
            d = d // 2
        else:
            d = d - 1
    if a + b + c + d == n:
        return True
    else:
        return False
