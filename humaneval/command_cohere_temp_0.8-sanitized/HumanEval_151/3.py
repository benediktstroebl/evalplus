def double_the_difference(lst):
    odd_numbers = [num for num in lst if num > 0 and num % 2 != 0]
    return sum(num ** 2 for num in odd_numbers if isinstance(num, int))