
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    #Initialize the four even numbers to zero
    a = b = c = d = 0
    # Check if the given number can be written as the sum of exactly 4 positive even numbers
    while n != a + b + c + d:
        # If the number can be written as the sum of exactly 4 positive even numbers
        if n == a + b + c + d:
            return True
        # If the number cannot be written as the sum of exactly 4 positive even numbers
        elif n < a + b + c + d:
            return False
        # Else, we increment a and try again
        else:
            a += 2
            b += 4
            c += 6
            d += 8
    return False
