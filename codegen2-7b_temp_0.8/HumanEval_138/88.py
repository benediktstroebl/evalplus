
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    sum_of_positive_evens = 0
    for i in range(1, n):
        if is_sum_of_positive_even(i):
            sum_of_positive_evens += i
    return sum_of_positive_evens ==
