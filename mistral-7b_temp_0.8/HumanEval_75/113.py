
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_list = []
    for i in range(1, 100):
        if is_prime(i):
            prime_list.append(i)
    # for i in range(1, 100):
    #     if is_prime(i):
    #         prime_list.append(i)
    # print(prime_list)
    return True if a in [x * y * z for x in prime_list for y in prime_list for z in prime_list] else False

