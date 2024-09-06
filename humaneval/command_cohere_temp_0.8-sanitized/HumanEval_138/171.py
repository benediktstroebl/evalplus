def is_equal_to_sum_even(n):
    even_numbers = [2, 4, 6, 8, 10, 12]
    sum_of_even = sum(even_numbers)
    if n == sum_of_even:
        return True
    return False