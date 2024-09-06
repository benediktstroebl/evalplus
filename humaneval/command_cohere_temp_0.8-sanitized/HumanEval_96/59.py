def count_up_to(n):
    primes = []
    num = 2
    while len(primes) < n:
        # checking divisibility evenly distribution up to sqrt(num)
        if num == 2:
            pass
        elif num == 3:
            primes.append(num)
        elif num > 3:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
        num += 1
    return primes[:n]