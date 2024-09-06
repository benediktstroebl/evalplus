def count_up_to(n):
    # Create a list to store the prime numbers up to n.
    primes = []
    # Iterate through integers from 2 up to n.
    for num in range(2, n+1):
        # Check if the number is prime and push to the list if it is.
        if is_prime(num):
            primes.append(num)
            if len(primes) == n:
                break
    return primes
def is_prime(n):
    # Check if the number is equal to 1 as it is not prime.
    if n == 1:
        return False
    # Check if the number is even and if so, check if it is divisible by 2.
    elif n % 2 == 0:
        return False
    # Iterate through integers up to the square root of the number.
    for i in range(3, int(n**0.5)+1, 2):
        # If the number is divisible by any number, return False.
        if n % i == 0:
            return False
    # If no divisors are found, return True.
    return True