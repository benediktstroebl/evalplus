def is_equal_to_sum_even(n):
    even_nums = [2 * x for x in range(1, (n // 2) + 1) if x % 2 == 0]
    return len(even_nums) == n // 4 and sum(even_nums) == n