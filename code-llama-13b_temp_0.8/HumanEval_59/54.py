

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # return the largest prime factor of n
    for i in range(2, n+1):
        if n%i==0:
            flag=1
            for j in range(2, i):
                if i%j==0:
                    flag=0
                    break
            if flag==1:
                return i

