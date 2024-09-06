
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        a_divisors = []
        for i in range(2, a):
            if a % i == 0:
                a_divisors.append(i)
        
        if len(a_divisors) == 3:
            for n in a_divisors:
                prime_divisors = []
                for i in range(2, n):
                    if n % i == 0:
                        prime_divisors.append(i)
                
                if len(prime_divisors) != 0:
                    return False
        else:
            return False
    
    return True
