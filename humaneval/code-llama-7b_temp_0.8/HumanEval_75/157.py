
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # we assume that is not the product of 3 prime number
    prime_numbers = [2]
    i = 2
    while prime_numbers[-1] <= 10:
        # we check if i is prime number
        is_prime = True
        for prime_number in prime_numbers:
            if i % prime_number == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(i)
        i += 1

    #we check if a is the product of 3 prime number
    for prime_number1 in prime_numbers:
        if a / prime_number1 > 10:
            return False
        for prime_number2 in prime_numbers:
            if (a / prime_number1) / prime_number2 > 10:
                return False
            if prime_number1 * prime_number2 == a:
                return True
    return False
