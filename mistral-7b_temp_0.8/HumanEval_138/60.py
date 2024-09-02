
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    """
    f(n):
    if n == 2: return False
    if n == 4: return True
    if n % 2 != 0: return False
    if f(n/2) == True: return True
    if n/2 % 2 != 0: return False
    return f(n/2)
    """
    #recursive
    #if n%2 != 0: return False
    #if n/2 % 2 != 0: return False
    #if n == 2: return False
    #if n == 4: return True
    #return f(n/2)

    #iterative
    if n == 2: return False
    if n == 4: return True
    if n % 2 != 0: return False
    else:
        temp = n/2
        while True:
            if temp == 4: return True
            if temp % 2 == 0:
                temp = temp/2
            else:
                return False
