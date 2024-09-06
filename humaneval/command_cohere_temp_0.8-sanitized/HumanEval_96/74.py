def count_up_to(n):
    # Check if n is 0 or 1, and return an empty list if so
    if n <= 1:
        return []
    # Initialize a list to store the prime numbers and count variable
    primes = []
    count = 0
    # Iterate through integers 2 through n
    for num in range(2, n+1):
        # Check for prime using the sieve of Eratosthenes
        if num == 2:
            primes.append(2)
            count += 1
        elif num % 2 == 0:
            # If divisible by 2, skip all even numbers
            while num % 2 == 0:
                num += 1
        else:
            # If not divisible by 2, mark all multiples as non-prime
            for i in range(3, int(num**0.5) + 1, 2):
                if num % i == 0:
                    while num % i == 0:
                        num += i - 1
                        break
            if num > 2:
                primes.append(num)
                count += 1
    return primes[:n]