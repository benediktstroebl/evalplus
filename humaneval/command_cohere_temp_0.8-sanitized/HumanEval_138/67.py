def is_equal_to_sum_even(n):
    even_nums = [2 * x for x in range(1, int(n**0.5) + 1)]
    return n == sum(even_nums)