
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    i = 0
    evens = []
    while i < 4:
        if n % 2 == 0:
            evens.append(n)
        else:
            i += 1
        n -= 1
    if sum(evens) == 4:
        return True
    return False
