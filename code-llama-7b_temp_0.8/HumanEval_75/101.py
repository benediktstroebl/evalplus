
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # print(a)
    prime_number = []
    prime_num = 2
    while prime_num < a:
        if is_prime(prime_num):
            prime_number.append(prime_num)
        prime_num += 1
    # print(prime_number)
    if len(prime_number) < 3:
        return False
    else:
        if prime_number[0] * prime_number[1] * prime_number[2] == a:
            return True
        else:
            return False
    


