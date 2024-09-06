
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    result = False
    for i in range(2, int(n/2 + 1)):
        sum = 0
        for j in range(i):
            sum += i
        if (sum == n):
            result = True
            break
    return result
