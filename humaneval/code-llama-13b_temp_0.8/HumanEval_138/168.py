
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    sum = 0
    counter = 0
    for i in range(n, 0, -2):
        counter = counter + 1
        sum = sum + i
        if sum == n:
            if counter == 4:
                return True
            else:
                return False
    return False


