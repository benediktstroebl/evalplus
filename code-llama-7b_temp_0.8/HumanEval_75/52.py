
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a > 100:
        return "a is greater than 100"
    prime_factor_list = []
    i = 2
    while True:
        if is_prime(i):
            prime_factor_list.append(i)
            if len(prime_factor_list) == 3:
                break
        i += 1
    return a == product(prime_factor_list)

