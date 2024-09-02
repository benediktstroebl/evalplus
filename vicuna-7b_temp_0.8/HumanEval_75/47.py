
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Create a list of all integers between 2 and a
    all_numbers = range(2, a+1)
    
    # Create a set of all prime numbers below a
    prime_numbers = set(range(2, int(a**0.5) + 1))
    
    # Create a dictionary that maps each number to its prime factors
    factors = {}
    for number in all_numbers:
        factors[number] = []
        for prime in prime_numbers:
            if number % prime == 0:
                factors[number].append(prime)
    
    # Loop through each number in the list and check if it's a prime factor of any number in the dictionary
    for number in all_numbers:
        if number in factors:
            for factor in factors[number]:
                if factor not in prime_numbers:
                    return False
            return True
    return False