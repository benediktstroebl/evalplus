
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    sum_of_evens = 0
    number_of_evens = 0
    while number_of_evens < 4:
        if sum_of_evens + 2 == n:
            return True
        elif sum_of_evens + 2 < n:
            sum_of_evens += 2
            number_of_evens += 1
        else:
            return False





