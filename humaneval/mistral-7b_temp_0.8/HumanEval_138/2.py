
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if(n%2!=0):
        return False
    elif(n>20):
        return False
    else:
        for i in range(2, n):
            if(n%i==0):
                if(i%2!=0 or i>4):
                    return False
                else:
                    n=n/i
                    return True


