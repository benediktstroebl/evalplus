def double_the_difference(numbers):
    odd_squares = sum(square for num in numbers for square in (num**2) if num % 2 and num >= 0 and isinstance(num, int))
    return max(odd_squares, 0)