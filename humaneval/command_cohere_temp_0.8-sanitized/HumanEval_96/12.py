def count_up_to(n):
    # Check if n is 0 or 1, and return an empty list if so
    if n <= 1:
        return []
    # Initialize a list to store the prime numbers and a variable to mark the current number
    primes = []
    current = 2
    # Loop through numbers up to n
    for num in range(2, n+1):
        # Skip all odd numbers because they can't be prime
        if num % 2 == 0:
            # Mark the current number as prime and add it to the list if it is less than n and only divisible by 1 and itself
            if current == 2 and num == current:
                primes.append(current)
            elif num > current and num % current == 0 and num / current < n:
                primes.append(current)
            current = num
    # Return the list of prime numbers
    return primes