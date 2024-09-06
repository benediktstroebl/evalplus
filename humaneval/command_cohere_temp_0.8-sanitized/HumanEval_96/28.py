def count_up_to(n):
    primes = []
    num = 2
    while len(primes) < n:
        # marking odd numbers as candidates
        for i in range(3, int(n**0.5)+1, 2):
            if num == i:
                continue
            # marking all numbers divisible by i as non-prime
            for j in range(i, 0, -1):
                if num % j == 0:
                    break
            else:
                primes.append(num)
        num += 1
    return primes