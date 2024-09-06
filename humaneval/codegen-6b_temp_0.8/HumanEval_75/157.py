
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def divisors(a):
        ret = []
        i = 1
        while i * i <= a:
            if a % i == 0:
                ret.append(i)
                ret.append(a // i)
            i += 1
        ret.sort(reverse=True)
        return ret
    # find all prime divisors
    primes = []
    for i in range(2, 101):
        if is_prime(i):
            primes.append(i)
    #if no 3 prime divisor, then it's not the product of 3 prime numbers
    if len(divisors(a)) == 0:
        return False
    # calculate a/n for all bigger or equal to len(primes)
    div = []
    for i in range(len(primes), 0, -1):
        try:
            div.append(a // primes[i-1])
        except:
            div.append(0)
    #calculate the products for the found prime divisors
    products = {}
    for i in range(len(div)):
        if div[i] != 0:
            products[primes[i-1]] = div[i]
    #since we know that a < 100, check if every entry in the products dict is a prime
    return all([i in primes for i in products.values()])
