def double_the_difference(numbers):
    odd_squares = sum(square for num in numbers if num % 2 and num >= 0 and isinstance(num, int))
    return int(odd_squares * 2) if odd_squares else 0