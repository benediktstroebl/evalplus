
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    num = n
    total = 0
    for i in range(1, n):
        if i % 2 == 0:
            total += i
            if total == num:
                return True
            elif total > num:
                break
    return False
