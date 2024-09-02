
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    i=2
    j=2
    k=2
    while(j<i):
        i=i+1
        while(k<j):
            k=k+1
            if (i*j*k==a):
                return True
        j=j+1
    return False
