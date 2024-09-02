
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    numbers = [1]
    number = 2
    while len(numbers) < 4:
        if is_even_to_sum_even(number):
            numbers.append(number)
        number += 1
    if n == sum(numbers):
        return True
    else:
        return False

