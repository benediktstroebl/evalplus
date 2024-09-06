def is_equal_to_sum_even(n):
    even_nums = [2 * x for x in range(1, (n // 2) + 1)]
    return n == sum(even_nums) and n == 4 * sum(even_nums)