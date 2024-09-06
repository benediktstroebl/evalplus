
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    a_list = list(get_primes(a))
    n = len(a_list)
    for i in range(n):
        for j in range(i+1, n):
            if a_list[i] * a_list[j] == a:
                return True
    return False
