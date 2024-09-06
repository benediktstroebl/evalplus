
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def sieve(n):
        flag = [True] * (n + 1)
        for i in range(2, len(flag)):
            for j in range(i * 2, len(flag), i):
                flag[j] = False
        return flag
    prime = sieve(100)
    for i in range(len(prime)):
        if prime[i] == True:
            for j in range(i + i, len(prime), i):
                if prime[j] == True:
                    if j % i == 0:
                        if j / i in prime:
                            if j != i:
                                if j / i == i:
                                    if j / i in prime:
                                        pass
                                else:
                                    prime[j] = False
    for i in range(1, len(prime)):
        if prime[i] == True:
            if a % i == 0:
                return True
    return False
