
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    a = 0
    b = 0
    c = 0
    d = 0
    if n % 2 != 0:
        return False
    for i in range(1, n // 2):
        for j in range(i + 1, n // 2):
            for k in range(j + 1, n // 2):
                for l in range(k + 1, n // 2):
                    if i + j + k + l == n:
                        a = i
                        b = j
                        c = k
                        d = l
                        return True
    return False

