
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    sum_of_evens = 0
    for i in range(0,n):
        if (i%2 == 0):
            sum_of_evens = sum_of_evens + i
    if (sum_of_evens == n):
        return True
    else:
        return False

