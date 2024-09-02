
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    
    numbers = []
    while n!= 0:
        if n % 2 == 0:
            numbers.append(n)
        n -= 1
    return len(numbers) == 4
    
