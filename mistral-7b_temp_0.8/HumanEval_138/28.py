
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 == 0:
        return False
    if n <= 2:
        return False
    # print(n)
    sum_even = 0
    current = 2
    while sum_even <= n:
        if n % current == 0:
            sum_even += current
            # print(n, sum_even)
            if sum_even == n:
                return True
        current += 2
    return False

