
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    for i in range(1, (n // 2) + 1): # excluding the last even number
        if (n - 4 * i) % 2 == 0: # if the difference between the given number and the sum of 4 positive even numbers is even, it can be written as the sum of 4 positive even numbers
            return True
    return False


