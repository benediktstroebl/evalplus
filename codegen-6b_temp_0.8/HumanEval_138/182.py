
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Your code here
    # Hint: you could use a helper function
    if n <= 0:
        return False
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 != 0:
        return False
    else:
        a = n/2
        while a % 2 == 0:
            a = a/2
        return True if a == 1 else False
    
    return False
