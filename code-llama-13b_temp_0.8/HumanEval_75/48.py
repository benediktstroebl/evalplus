
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # your code here
    prime = [2,3,5,7,11,13,17,19]
    for i in range(len(prime)):
        if a%prime[i] == 0:
            a /= prime[i]
        else:
            return False
    return True
