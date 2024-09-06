def count_up_to(n):
    # Create a list to store the prime numbers up to n.
    primes = []
    # Iterate through integers from 2 up to n.
    for num in range(2, n + 1):
        # Check if the number is prime and append it to the list if so.
        if is_prime(num):
            primes.append(num)
            if len(primes) == n:
                break
    return primes
def is_prime(num):
    # Check if the number is equal to 1, as it is not a prime number.
    if num == 1:
        return False
    # Check if the number is even, if so, it includes at least one even integer.
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        # Check if the number is divisible by any odd integer, if so it is not prime.
        if num % i == 0:
            return False
    return True