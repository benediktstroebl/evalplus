def is_multiply_prime(a):
    # check if a is less than 100
    if a < 100:
        # check if the root of a is an integer
        if int(root(a)) == a: 
            # check if the root is a prime number
            if is_prime(a):
                # check if a can be written as a product of 3 prime factors
                if a != 1 and a != 3 and a != 107:
                    return True
    return False
def root(n):
    # return the root of n
    return int(n ** 0.5)
def is_prime(n):
    # check if n is less than 100 and is prime
    if n < 100 and n != 1 and n != 107:
        # check if the number has divisor except 1 and itself
        if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
            return False
        i = 7
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    return False