
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    a_str = str(a)
    primes = [2, 3, 5]
    check_str = ""
    for num in primes:
        check_str += str(num)
        if len(check_str) == len(a_str):
            return False
        if check_str in a_str:
            continue
        else:
            return False
    return True
