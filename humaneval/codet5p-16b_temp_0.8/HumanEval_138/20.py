
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    n = abs(n) # make sure the given number is positive
    even_numbers = [2, 4, 6, 8]
    i = 0
    while i < len(even_numbers):
        if n == even_numbers[i]: # if the sum of the 4 numbers equals the given number n
            return True
        if n > even_numbers[i]: # if the sum of the 4 numbers is greater than the given number n
            i += 1 # try the next number
        else:
            return False
