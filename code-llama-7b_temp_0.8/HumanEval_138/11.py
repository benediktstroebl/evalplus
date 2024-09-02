
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    even = []

    for i in range(1, n + 1):
        if i % 2 == 0:
            even.append(i)

    if len(even) > 4:
        return False

    for i in range(len(even) - 1):
        for j in range(i + 1, len(even)):
            for k in range(j + 1, len(even)):
                for m in range(k + 1, len(even)):
                    if even[i] + even[j] + even[k] + even[m] == n:
                        return True
    return False
