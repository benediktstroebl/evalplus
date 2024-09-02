

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """

    num_div_11 = n // 11
    num_div_13 = n // 13
    multiples_11 = 11 * list(range(1, num_div_11))
    multiples_13 = 13 * list(range(1, num_div_13))
    multiples_77 = 7 * multiples_13
    sum_77 = sum(multiples_77)

    total = n - sum_77

    multiples_11 = 11 * list(range(1, num_div_11))
    multiples_13 = 13 * list(range(1, num_div_13))
    multiples_7 = 7 * list(range(1, num_div_11))
    sum_7 = sum(multiples_7)

    total -= sum_7

    return total
