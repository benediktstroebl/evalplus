
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if not type(n) == int:
        return False
    if n % 2 != 0 or n < 0 or n <= 3:
        return False
    a = 0
    b = 0
    c = 0
    d = 0
    sum = 0
    if n == 8:
        return True
    for i in range(1, n // 2 + 1):
        if i % 2 == 0 and n - i % 2 == 0 and n - i >= 0 and n - i != n // 2:
            a = i
            b = n - i
            c = n - a
            d = n - b
            sum = a + b + c + d
            if sum == n:
                return True
    return False

