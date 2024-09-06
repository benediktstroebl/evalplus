
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    is_prime = lambda num: num > 1 and all(num % i!= 0 for i in range(2, num))
    primes = []
    for i in range(2,a):
        if is_prime(i):
            primes.append(i)
    if len(primes) == 3:
        print("True")
    else:
        print("False")

    
    

    
    



    

    

    
    

    
    

    

    

    
    

    
    

    
    

    
    

    
    

    
    

    
    

    
    
    

    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
