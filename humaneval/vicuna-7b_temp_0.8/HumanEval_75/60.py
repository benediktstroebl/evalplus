
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Use a dictionary to store the prime numbers and their counts
    prime_count = {2: 2, 3: 2, 5: 1, 7: 1, 11: 1, 13: 1, 17: 1, 19: 1, 23: 1, 29: 1, 31: 1}

    # Use a counter to keep track of the number of factors of a number
    def count_factors(n):
        factors = {}
        for i in range(1, n + 1):
            if n % i in factors:
                factors[i] = factors[i] + 1
        return factors

    # Use the is_prime function to check if the given number is prime
    if a % 2 == 0:
        return False
    if a in prime_count:
        # If the number is prime, check if it can be divided by 3
        if a % 3 == 0:
            return False
        else:
            # If the number is not divisible by 3, check if it can be divided by 5
            if a % 5 == 0:
                return False
            else:
                # If the number is not divisible by 3 or 5, it must be prime
                return True
    else:
        # If the number is not in the dictionary, it is not prime
        return False
