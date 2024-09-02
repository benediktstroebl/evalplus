
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_list = []
    i = 2
    while i < 100:
        if is_prime(i):
            prime_list.append(i)
        i += 1
    return a in list(set(prime_list) * 3)
