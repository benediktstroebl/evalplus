
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    def is_prime(number):
        for i in range(2, int(number**(1/2))+1):
            if number % i == 0:
                return False
        return True

    prime_numbers = []
    for i in range(2, 100):
        if is_prime(i):
            prime_numbers.append(i)

    if a % 2 == 0:
        prime_numbers.remove(2)
    if a % 3 == 0:
        prime_numbers.remove(3)

    if a % 5 == 0:
        prime_numbers.remove(5)

    if a % 7 == 0:
        prime_numbers.remove(7)

    for prime in prime_numbers:
        if a % prime == 0:
            return False
    return True
