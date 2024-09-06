def count_up_to(n):
    # Initialize an array to store the prime numbers
    primes = []
    # Iterate through the numbers from 2 to n
    for num in range(2, n + 1):
        # Check if the number is prime by testing all possible divisors from 2 to the square root of the number
        is_prime = True
        for d in range(2, int(num ** 0.5) + 1):
            if num % d == 0:
                is_prime = False
                break
        # If the number is prime, add it to the array
        if is_prime:
            primes.append(num)
    # Return the array of prime numbers
    return primes