
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(a):
        factor = 2
        while factor <= a:
            if a % factor == 0:
                return False
            else:
                factor += 1
        return True 
    
    def factorization(a):
        if a < 2:
            return 1
        primefactors = []
        for i in xrange(2,a):
            if a % i == 0:
                while a % i == 0:
                    a //= i
                    primefactors.append(i)
        if a > 2:
            primefactors.append(a)
        return tuple(primefactors)

    primefactors = factorization(a)
    for i in xrange(0,len(primefactors)):
        if is_prime(primefactors[i]) == False:
            return False
    return True

