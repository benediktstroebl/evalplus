
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_list = []
    for i in range(2,a+1):
        if a % i == 0:
            prime_list.append(i)

    if len(prime_list) != 3:
        return False
    else:
        return True

