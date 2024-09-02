
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def isPrime(x):
        if x < 2:
            return False
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    num = a
    while num > 99:
        if num % 3 == 0:
            if isPrime(num) and isPrime(num/3):
                num /= 3
            else:
                return False
        else:
            num -= 1
    if num == 3:
        return True
    return False
