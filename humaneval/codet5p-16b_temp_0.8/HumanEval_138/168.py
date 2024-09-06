
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    
    n = str(n)
    even_sum = 0
    even_numbers = [2]
    
    for digit in n:
        even_sum += int(digit)
        
    for i in range(1, 5):
        if even_sum - (i * 2) in even_numbers:
            return True
            break
            
    return False
    
