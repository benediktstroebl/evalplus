
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    #decompose number
    prime_numbers = []
    i = 2
    while i < a:
        if is_prime(i):
            prime_numbers.append(i)
        i+=1
    print(prime_numbers)

    #check if three primes
    if len(prime_numbers) < 3:
        return False
    elif len(prime_numbers) > 3:
        return False
    else:
        if a == prime_numbers[0] * prime_numbers[1] * prime_numbers[2]:
            return True
        else:
            return False
