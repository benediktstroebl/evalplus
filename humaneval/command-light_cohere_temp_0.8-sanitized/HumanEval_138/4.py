def is_equal_to_sum_even(n):
    return n % 4 == 0 and sum(x % 2 for x in range(1, n + 1)) % 4 == 0