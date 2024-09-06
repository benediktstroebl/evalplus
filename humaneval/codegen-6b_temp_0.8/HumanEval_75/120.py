
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    
    prob_num = a
    while prob_num > 1:
        divide_value = 0
        while prob_num % 2 == 0:
            divide_value += 1
            prob_num /= 2
        prob_num = 3 ** divide_value * prob_num
        if prob_num == 1:
            return False
        else:
            divide_value = 0
            while prob_num % 3 == 0:
                divide_value += 1
                prob_num /= 3
            prob_num = 5 ** divide_value * prob_num
            if prob_num == 1:
                return False
    return True
