
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    numbers = [2, 4]
    while True:
        if n < 2: return False
        for num in numbers:
            if num * len(numbers) == n:
                return True
        n += 2
        numbers.append(n)

