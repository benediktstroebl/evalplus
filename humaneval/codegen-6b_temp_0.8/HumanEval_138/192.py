
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    result = False
    for i in xrange(n/2, n, 2):
        if is_even(i):
            aux = n - 2 * i
            if is_even(aux):
                if aux == i:
                    result = True
                    break
    return result

