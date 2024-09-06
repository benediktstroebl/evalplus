
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n == 0:
        return True
    if n < 0:
        return False
    if n % 2 == 1:
        return False
    
    left = n // 2
    right = n // 2 + 1

    while left > 0:
        for i in range(1, 5):
            if left < i:
                return False
            if left % i == 0:
                num1 = left // i
                num2 = left - num1
                if num1 % 2 == 0 and num2 % 2 == 0:
                    return True
        left -= 1

    return False
