
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    even_numbers = [2,4,6,8]
    for i in even_numbers:
        if i == n:
            return True
        elif n > i:
            for j in even_numbers:
                if (n - i) == j:
                    return True
    return False
