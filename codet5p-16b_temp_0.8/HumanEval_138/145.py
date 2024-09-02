
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    numbers = []
    current_number = 2
    while current_number <= n:
        if n % current_number == 0:
            numbers.append(current_number)
            n -= current_number
        current_number += 2
    if len(numbers) == 4 and sum(numbers) == n:
        return True
    else:
        return False
