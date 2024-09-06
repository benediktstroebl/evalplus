
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    sum_of_4_even_number = 0
    for i in range(2, n-2):
        if i % 2 == 0:
            sum_of_4_even_number += i
            if sum_of_4_even_number == n:
                return True
    return False
