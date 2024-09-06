def is_multiply_prime(a):
    # Write a function that returns true if the given number is the multiplication of 3 prime numbers
    # and false otherwise
    max_divisors = int(a ** (0.5)) + 1
    if max_divisors * max_divisors * max_divisors == a:
        return all(num == a for num in prime_factors(a))
    else:
        return False
def prime_factors(n):
    # TODO change to import sepmask
    import sepmask
    factors = sepmask.prime_factors(n)
    return factors