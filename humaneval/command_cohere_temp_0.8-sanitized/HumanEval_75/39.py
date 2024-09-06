def is_multiply_prime(a):
    # Check if a is a perfect square
    root = int(pow(a, 0.5))
    if root * root == a and a != 1:
        return False

    # Check for divisors
    for i in range(2, root + 1):
        if a % i == 0:
            return False

    # Check if a is the product of 3 primes
    for i in range(2, a // 2 + 1):
        if a % i == 0 and a != i and a != i * i:
            return False
    
    return True