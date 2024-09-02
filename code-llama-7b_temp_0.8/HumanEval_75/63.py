
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    a_factor=0
    for i in range(1, a+1):
        if (a%i==0):
            a_factor+=1
    if a_factor==3:
        return True
    else:
        return False
