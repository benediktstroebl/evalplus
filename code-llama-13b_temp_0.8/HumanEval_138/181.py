
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n == 0:
        return False
    if n == 2:
        return True

    sum = 2
    for i in range(3, n):
        if i % 2 == 1:
            continue
        if i % 4 == 0:
            continue
        if sum + i == n:
            return True
        elif sum + i > n:
            break

    return False

