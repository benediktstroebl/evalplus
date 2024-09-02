
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # TODO: Use sum and filter
    #raise Exception("Not implemented yet.")
    result = False
    evens = [i for i in range(n, 0, -2) if i % 2 == 0]
    if len(evens) == 4:
        if sum(evens) == n:
            result = True
    return result
