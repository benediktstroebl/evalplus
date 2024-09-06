
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def isprime(n):
        if n % 2 == 0 and n > 2:
            return False
        return all(n%i for i in range(3,int(n**0.5)+1,2))

    prime_numbers = [1,2,3,5,7]
    for i in range(2,len(prime_numbers)):
        if prime_numbers[i] > 10**6:
            break
        for j in range(2,len(prime_numbers)):
            if prime_numbers[j] > 10**6:
                break
            if i * j == a:
                return isprime(a) and isprime(i) and isprime(j)
    return False
