def count_up_to(n):
    primes = []
    seen = set()
    for num in range(2, n+1):
        is_prime = True
        for possible_divisor in range(2, int(num**0.5)+1):
            if possible_divisor > num // possible_divisor:
                break
            if num % possible_divisor == 0:
                is_prime = False
                break
        if is_prime:
            if num not in seen:
                primes.append(num)
                seen.add(num)
    return primes