
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    if n % 2!= 0:
        return False
    number_of_even_numbers = 4
    sum_of_numbers = 0
    for i in range(0,number_of_even_numbers):
        sum_of_numbers += i
    if sum_of_numbers == n:
        return True
    return False

