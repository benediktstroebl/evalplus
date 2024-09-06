def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100 and a > 1:
        prime_factors = []
        while a % 2 == 0:
            prime_factors.append(2)
            a = a // 2
        for i in range(3, int(a ** 0.5) + 1, 2):
            while a % i == 0:
                prime_factors.append(i)
                a = a // i
        if a > 2:
            prime_factors.append(a)
        return len(prime_factors) == 3
    return False