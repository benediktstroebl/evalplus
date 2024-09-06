def count_up_to(n):
    # check if n is 0 or 1, if so, return an empty list
    if n <= 1:
        return []
    # Initialize a list to store the prime numbers and count variable
    primes = []
    count = 0
    # Iterate through integers 2 through n
    for num in range(2, n + 1):
        # Check for prime using the sieve of Eratosthenes
        if num == 2:
            primes.append(num)
            count += 1
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            count += 1
    return primes[:n]