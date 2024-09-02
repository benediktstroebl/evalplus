
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    num_set = set()
    while n > 0:
        num = n % 10
        if num in num_set:
            return False
        else:
            num_set.add(num)
            n = n // 10
    if len(num_set) != 4:
        return False
    if 2 not in num_set:
        return False
    return True


