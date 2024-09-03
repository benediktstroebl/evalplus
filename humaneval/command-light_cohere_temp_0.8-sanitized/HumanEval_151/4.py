def double_the_difference(numbers):
    odd_nums = [num for num in numbers if num % 2 == 1]
    odd_squares = sum([num ** 2 for num in odd_nums])
    return odd_squares