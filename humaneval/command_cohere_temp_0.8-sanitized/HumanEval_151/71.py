def double_the_difference(numbers):
    odd_squares = 0

    for num in numbers:
        if num % 2 != 0 and isinstance(num, int) and num >= 0:
            odd_squares += num ** 2

    return odd_squares