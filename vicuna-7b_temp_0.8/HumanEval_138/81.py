
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n <= 4:
        return False
    elif n % 2 == 0 and n > 4:
        for i in range(3, (n + 1) // 2):
            if n - i in [2, 4, 6, 8]:
                return False
        return True
    else:
        return False

@checker(is_equal_to_sum_even, lambda n: int(input().strip()))
