
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # define the prime numbers
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    # the list to store the factors
    factors = []
    # get the square root of the given number
    root = int(a ** (1 / 2))
    # check if the given number is a prime number
    if a in prime:
        return True
    # if the given number is not a prime number, check the list of prime numbers
    for i in prime:
        # check if the given number is not equal to 1
        if a != 1:
            # check if the given number is divisable by the prime number
            if a % i == 0:
                # check if the prime number is less than the square root
