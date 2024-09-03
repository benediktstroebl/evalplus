def count_up_to(n):
    """Return an array of the first n integers that are prime numbers and less than n"""
    limit = n + 1
    prime_numbers = []
    for num in range(2, limit):
        is_prime = True
        for p in range(2, int(num ** 0.5) + 1):
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
    return prime_numbers