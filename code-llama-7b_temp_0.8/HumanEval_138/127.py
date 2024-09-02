
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    x = n
    count = 0
    sum = 0
    while x >= 2:
        if x % 2 == 0:
            sum += x
            count += 1
        x -= 1
    if count == 4:
        return True
    else:
        return False
