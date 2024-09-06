
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    numbers = set()
    while True:
        if len(numbers) == 4:
            break
        current_numbers = [n - i for i in numbers]
        if any(number < 0 or number % 2!= 0 for number in current_numbers):
            continue
        numbers.add(n - sum(current_numbers))
    return sum(numbers) == n
    
    
