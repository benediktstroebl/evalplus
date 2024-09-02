
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    multiply_of_three = True
    prime_factors = []
    for i in range(2, a + 1):
        if i!= 2 and i!= 3 and i!= 5:
            if a % i == 0:
                prime_factors.append(i)
    if len(prime_factors) > 1:
        multiply_of_three = False
    return multiply_of_three
    
    
    
