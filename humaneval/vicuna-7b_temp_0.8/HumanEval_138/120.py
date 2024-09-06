
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Define a variable to hold the number of even summands
    even_sum = 0
    
    # Check if n is even
    if n % 2 == 0:
        even_sum += 2

    # Check if n is 4 or 6
    if n in [4, 6]:
        if n % 2 != 0:
            return False
        else:
            even_sum += n // 2
    
    # Check if n is 8
    if n == 8:
        if n % 2 != 0:
            return False
        else:
            even_sum += n // 2
    
    # Check if n is equal to the sum of exactly 4 even numbers
    if even_sum == 4:
        return True
    else:
        return False
