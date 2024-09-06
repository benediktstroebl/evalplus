def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12]
    sum_n = 0
    for num in even_nums:
        sum_n += num
    return n == sum_n