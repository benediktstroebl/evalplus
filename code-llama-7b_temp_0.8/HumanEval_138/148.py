
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    even_numbers = [2, 4, 6, 8]
    result = []
    for num in even_numbers:
        if num == n:
            return True
        elif num < n:
            result.append(n - num)
        elif num > n:
            return False
    return is_equal_to_sum_even(result[0]) if result else False

