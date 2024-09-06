def count_up_to(n):
    primes = []
    # Loop to find primes smaller than N
    for i in range(2, n + 1):
        is_prime = True
        # Check if the number is divisible by any number till its square
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        if len(primes) == n:
            break
    return primes