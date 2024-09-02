
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # ! start your code !
    even_number = [2, 4, 6, 8]
    for i in range(2, n - 2):
        for j in range(4):
            if i + even_number[j] == n:
                return True
    return False
    # ! end your code !

