
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 != 0:
        return False
    if n < 16:
        return False
    else:
        sum = 0
        for i in range(1, 9):
            if i < 5:
                sum += i
            elif i == 5:
                sum += 10
            else:
                sum += 12
            if sum == n:
                return True
    return False
