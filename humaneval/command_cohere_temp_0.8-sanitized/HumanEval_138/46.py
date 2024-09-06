def is_equal_to_sum_even(n):
    even_nums = [2 * x for x in range(1, int(n**0.5) + 1) if x ** 2 <= n]
    return len(even_nums) == 4 and sum(even_nums) == n