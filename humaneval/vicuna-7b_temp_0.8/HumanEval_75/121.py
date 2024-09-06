
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(x):
        if x < 2:
            return False
        for p in range(2, int(x**0.5) + 1):
            if x % p == 0:
                return False
        return True
    
    def is_multiple(n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False
    
    a = int(a)
    p = 5
    for i in range(1, int(a**0.5) + 1):
        if is_prime(p) and is_multiple(p):
            p = int(p)
        elif is_prime(a) and is_multiple(a):
            a = int(a)
        elif is_prime(p) and is_prime(a) and p % a == 0:
            return True
        else:
            p = int(p)
    return False

print(is_multiply_prime(30)) # should be True
print(is_multiply_prime(9)) # should be False