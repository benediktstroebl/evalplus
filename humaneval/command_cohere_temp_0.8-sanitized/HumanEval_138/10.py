def is_equal_to_sum_even(n):
    even_nums = [2 * i for i in range(1, int(n ** 0.5) + 1)]
    return len(even_nums) == 4 and n == sum(even_nums)