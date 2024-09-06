
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n <= 0:
        return False

    n_even = n % 2 == 0
    n_small = n < 4
    if n_even and n_small:
        return False
    if not n_even:
        n += 1

    for i in range(2, n):
        for j in range(2, n):
            for k in range(2, n):
                for l in range(2, n):
                    if i + j + k + l == n:
                        return True

    return False

