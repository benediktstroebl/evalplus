
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    is_sum_even = False
    evens = [2]
    while not is_sum_even:
        for n in range(len(evens)):
            evens[n] += 2
            if sum(evens) == n:
                is_sum_even = True
            else:
                is_sum_even = False
    return is_sum_even
