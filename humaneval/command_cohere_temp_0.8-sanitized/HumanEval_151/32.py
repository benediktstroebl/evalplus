def double_the_difference(numbers):
    odd_squares = 0
    
    for num in numbers:
        if isinstance(num, int) and num % 2:
            odd_squares += num ** 2
    
    return odd_squares