
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    
    def isPrime(a):
        if a < 2:
            return False
        elif a == 2 or a == 3:
            return True
        elif a % 2 == 0:
            return False
        elif a < 9:
            return True
        else:
            # print(a)
            for i in range(3, int(a**0.5) + 1, 2):
                if a % i == 0:
                    return False
            return True
    
    # print(a)
    
    a_prime = [2, 3]
    # a_prime = [2]
    
    if a < 100:
        for divisor in range(2, a//2 + 1):
            if a % divisor == 0:
                if isPrime(divisor):
                    a_prime.append(divisor)
        if len(a_prime) == 3:
            return True
        else:
            return False
    else:
        for divisor in a_prime:
            if a % divisor == 0:
                return False
        return True
