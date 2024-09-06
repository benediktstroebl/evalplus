
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    
    # Using the sieve of Eratosthenes...
    prime = [True] * 100
    for i in range(2, 100):
        if prime[i]:
            for j in range(i*2, 100, i):
                prime[j] = False

    # how much of a prooblem is this?
    # a better way to do it would be
    # to check all permutations of the 3-digit number
    # and see if they're divisible by 7 and 5