
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if not isinstance(n, int):
        raise TypeError(f"{n} is not an integer")

    if n < 2:
        raise ValueError(f"{n} is less than 2")

    for i in range(1, n - 1):
        for j in range(i + 1, n):
            if is_even(i) and is_even(j):
                sum = i + j
                if sum == n:
                    return True
    return False

