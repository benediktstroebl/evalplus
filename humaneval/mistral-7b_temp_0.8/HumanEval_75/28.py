
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    #return "This function has not been implemented yet"
    if a > 0 and a < 100:
        result = True
        for i in range(2, a):
            if a % i == 0:
                result = False
        return result
    else:
        return "Error: Given Number is not in the range of 2 to 100"
