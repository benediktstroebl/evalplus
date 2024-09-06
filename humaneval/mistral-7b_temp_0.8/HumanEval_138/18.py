
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n%2 != 0:
        return False
    if n <= 4:
        return False
    sum_of_even = 0
    i = 0
    while i < n:
        if n%i == 0:
            if i%2 == 0:
                sum_of_even += i
            i += 1
        else:
            i += 1
    if sum_of_even == n:
        return True
    else:
        return False
