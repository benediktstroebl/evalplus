
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 == 1:
        return False
    for i in range(1, n + 1):
        if i % 2 != 0:
            continue
        for j in range(1, n + 1):
            if j % 2 != 0:
                continue
            for k in range(1, n + 1):
                if k % 2 != 0:
                    continue
                for l in range(1, n + 1):
                    if l % 2 != 0:
                        continue
                    if i + j + k + l == n:
                        return True
    return False
