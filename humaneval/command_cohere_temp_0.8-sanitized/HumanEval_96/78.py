def count_up_to(n):
    # Check if n is less than 2, which does not trigger any elements for the counter
    if n < 2:
        return []
    # Creating a counter to count the first n prime numbers less than n and initializing it to 0
    prime_counter = 0
    # Iterating through the numbers from 2 to n-1, 2 is the smallest prime number and n-1 is the last potential prime number that can be used (excluding n itself since the task is to return the first n primes)