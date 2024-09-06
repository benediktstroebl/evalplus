
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # base case: if n <= 4, it is not possible to write n as the sum of 4 positive even numbers
    if n <= 4:
        return False
    
    # case: if n is 6 or 8, it can be written as the sum of 4 positive even numbers
    elif n in (6, 8):
        return True
    
    # loop: if n is not 6 or 8, we check all possible even numbers to see if they sum up to n
    else:
        total = 0
        for i in range(3, (n + 1) // 2):
            total += i
        
        # if the total is equal to n, it can be written as the sum of 4 positive even numbers
        if total == n:
            return True
        
        # if the total is not equal to n, it cannot be written as the sum of 4 positive even numbers
        return False
