
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    sum_even = sum(
        [
            x
            for x in range(2, int(math.sqrt(n)) + 1, 2)
            if math.sqrt(n) % x == 0 and x % 2 == 0
        ]
    )

    return sum_even ==
