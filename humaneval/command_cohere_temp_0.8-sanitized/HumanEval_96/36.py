def count_up_to(n):
    primes = []
    # Iterate through numbers 2 through n
    for num in range(2, n + 1):
        # Iterate through each number to check its divisibility
        # Record ones that can't be divided by any number except 1 and itself
        for i in range(2, int(num**(0.5)) + 1):
            if num % i == 0:
                break
        else:
            # If no such number exists, it's a prime
            primes.append(num)
    return primes
n = 18