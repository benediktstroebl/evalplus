
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n == 0:
        return True
    elif n < 0:
        return False
    elif n % 2 != 0:
        return False

    sums = set()
    for i in range(1, (n//2) + 1):
        j = n - i
        if i >= j:
            continue
        if i + j in sums:
            return True
        else:
            sums.add(i + j)
    return False
