
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_number_list = sieve_of_eratosthenes(100)
    for i in range(len(prime_number_list)):
        for j in range(i+1, len(prime_number_list)):
            if prime_number_list[i] * prime_number_list[j] == a:
                return True
    return False

