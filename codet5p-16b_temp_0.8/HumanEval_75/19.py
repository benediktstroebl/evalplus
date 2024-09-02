
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    is_prime_number = lambda x: 0!= x % x
    result = False
    for i in range(3, a):
        if result == True:
            break
        if a % i == 0 and is_prime_number(i):
            a //= i
            i = 2
            while a % i == 0 and is_prime_number(i):
                a //= i
                i -= 1
                if a == 1:
                    result = True
                    break
            else:
                continue
            break
    return result

