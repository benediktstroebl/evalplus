
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    def is_even(n):
        return n % 2 == 0

    if is_even(n) == False:
        return False

    n_evens = list(filter(is_even, [n]))
    n_evens_sorted = sorted(n_evens)
    if len(n_evens_sorted)!= 4:
        return False
    if sum(n_evens_sorted)!= n:
        return False

    return True

