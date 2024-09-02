
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if (n % 2) != 0:
        return False
    for i in range(1, n):
        if i % 2 != 0:
            continue
        for j in range(i, n):
            if j % 2 != 0:
                continue
            for k in range(j, n):
                if k % 2 != 0:
                    continue
                for l in range(k, n):
                    if l % 2 != 0:
                        continue
                    if n == (i + j + k + l):
                        return True
    return False

