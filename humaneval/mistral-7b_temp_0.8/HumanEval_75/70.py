
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if(a<100 and a%2==0):
        return False
    prime = True
    for i in range(3,int(a**0.5),2):
        if(a%i==0):
            prime = False
            break
    if(prime):
        return False
    else:
        return True
