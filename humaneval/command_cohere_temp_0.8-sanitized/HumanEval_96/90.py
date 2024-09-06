def count_up_to(n):
    primes = []
    num = 2
    while len(primes) < n:
        # iterating until we find a prime or exceed n
        if num > n:
            break
        elif num == 2:
            primes.append(num)
        elif num % 2 == 0:
            continue
        else:
            primes.append(num)
            num += 1
        if len(primes) == n:
            break
    return primes