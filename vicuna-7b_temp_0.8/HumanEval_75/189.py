
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Create list of prime numbers less than a
    prime_list = [i for i in range(2, a) if is_prime(i)]
    
    # Check if the last prime number in the list is greater than a/2
    last_prime = prime_list[-1]
    if last_prime > a/2:
        return False
    
    # Check if the sum of all primes in the list is equal to a
    total = 0
    for i in prime_list:
        total += i
    if total != a:
        return False
    
    # If the above two conditions are met, the number is a multiplication of 3 prime numbers
    return True

a = 50
result = is_multiply_prime(a)
