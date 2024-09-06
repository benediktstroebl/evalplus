
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # best way to do this is to find the prime number
    # that is divisible by the number
    # find the prime number that is divisible by 3
    # and find the prime number that is divisible by 5
    # multiply these two together
    # This way is O(n) time complexity
    #
    # seconds to solve: 1.928s
    primes = [2,3,5,7,11,13,17]
    for p in primes:
        if a % p == 0:
            if a > 3 and a % 2 == 0:
                return False
            else:
                return True
    return False
