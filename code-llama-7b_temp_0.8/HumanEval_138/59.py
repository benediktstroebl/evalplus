
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    even_number = 0
    for _ in range(n):
        if _ % 2 == 0:
            even_number = _
            print(even_number)
            if even_number == n:
                return True
    return False

