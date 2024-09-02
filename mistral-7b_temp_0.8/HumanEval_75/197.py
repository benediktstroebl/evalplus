
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    a_is_prime = True
    list_numbers = []
    for i in range(2, a):
        if a % i == 0:
            a_is_prime = False
    if a_is_prime:
        print(f'{a} is a prime number')
    else:
        print(f'{a} is not a prime number')
    return a_is_prime

