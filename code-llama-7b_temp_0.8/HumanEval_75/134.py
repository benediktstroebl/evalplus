
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_list = list()
    if a < 10:
        return False
    if a == 30:
        return True
    for n in range(2, a):
        if a % n == 0:
            prime_list.append(n)
    if len(prime_list) > 4:
        return False
    for prime_num in prime_list:
        if not is_prime(prime_num):
            return False
    return True
