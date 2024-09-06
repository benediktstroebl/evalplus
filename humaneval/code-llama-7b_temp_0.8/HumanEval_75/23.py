
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # the function should look like:
    # def is_multiply_prime(a):
        # 1- check if a is prime, if not, return False
        # 2- check if (a/p)%p == 0
        # 3- repeat steps 2-3 for the next prime
        # 4- return True

    if a < 100:
        if a % 2 == 0 and a != 2:
            return False
        for i in range(3, int(a**(1/2))+1, 2):
            if a % i == 0:
                return False
        return True
    return 'The number must be less than 100'
