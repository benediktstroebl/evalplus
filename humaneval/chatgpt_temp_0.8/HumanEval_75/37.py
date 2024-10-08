def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    prime_count = 0
    for i in range(2, a):
        if is_prime(i) and a % i == 0:
            prime_count += 1
    return prime_count == 3
