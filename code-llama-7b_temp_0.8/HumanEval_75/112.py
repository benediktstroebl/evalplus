
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # find a's prime factors
    factors = []
    for i in range(2, a):
        if a%i == 0:
            factors.append(i)
    print(factors)
    # check if each factor is prime
    for i in factors:
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            factors.remove(i)
    print(factors)
    if len(factors) == 3:
        return True
    else:
        return False

