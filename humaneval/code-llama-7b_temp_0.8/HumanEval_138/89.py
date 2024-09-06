
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n <= 0:
        return False
    elif n % 2 != 0:
        return False
    else:
        numbers = []
        for i in range(2, int(n / 2) + 1):
            if i * 2 in numbers or (n - i * 2) in numbers:
                return True
            else:
                numbers.append(i * 2)
        return False
