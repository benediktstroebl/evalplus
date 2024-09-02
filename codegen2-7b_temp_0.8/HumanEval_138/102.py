
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    total = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            total += i
    if total == n:
        return True
    else:
        return
