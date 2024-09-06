def is_multiply_prime(a):
    # Check if a is less than 100
    if a < 100:
        # Check if a is the product of exactly 3 prime numbers
        prime_factors = []
        for i in range(2, int(a ** 0.5) + 1):
            while a % i == 0:
                prime_factors.append(i)
                a //= i
                if a == 1:
                    break
        if len(prime_factors) == 3 and a == 1:
            return True
    return False