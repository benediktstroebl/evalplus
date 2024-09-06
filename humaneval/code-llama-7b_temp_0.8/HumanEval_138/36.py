
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n <= 0 or n % 2 != 0:
        return False
    sum_even = n
    for i in range(1,n//2+1):
        if sum_even - 2*i >= 0:
            sum_even -= 2*i
        else:
            return False
    if sum_even == 0:
        return True
    return False
