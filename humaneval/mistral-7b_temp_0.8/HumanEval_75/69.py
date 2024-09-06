
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_list = []
    for i in range(2, 100):
        if is_prime(i):
            prime_list.append(i)
    for j in prime_list:
        if a % j == 0:
            a = a // j
    if a == 1:
        return True
    else:
        return False
