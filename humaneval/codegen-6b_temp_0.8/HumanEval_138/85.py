
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    numbers = []
    while n%2 == 0:
        numbers.append(2)
        n -= 2
    
    if n < 0:
        return False
    if n > 0:
        for i in range( 1,n+1 ):
            if n%i == 0:
                numbers.append(i)
    
    if len(numbers) == 4:
        return True
    else:
        return False


