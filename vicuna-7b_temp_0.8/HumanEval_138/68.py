
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # base case
    if n < 4:
        return True

    # find sum of even numbers less than n
    sum_of_even = 0
    for i in range(2, n // 2 + 1):
        sum_of_even += i

    # check if n is equal to sum of even numbers
    return n == sum_of_even
