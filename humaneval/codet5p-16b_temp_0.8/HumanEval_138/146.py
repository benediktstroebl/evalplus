
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    possible_numbers = [2 * x for x in range(1, n // 2)]
    possible_sums = [sum(possible_numbers[:i + 1]) for i in range(len(possible_numbers))]
    return n in possible_sums

