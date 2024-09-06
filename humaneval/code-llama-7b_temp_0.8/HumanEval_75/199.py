
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # your code here
    primes = [2, 3, 5]
    if a < 100:
        for i in range(len(primes)):
            if a == primes[i]:
                return True
            if a % primes[i] == 0:
                a = a / primes[i]
                i += 1
                if i > 1:
                    break
        return False
