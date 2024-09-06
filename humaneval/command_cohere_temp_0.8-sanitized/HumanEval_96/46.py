def count_up_to(n):
    # Create a list to store the prime numbers up to n.
    prime_numbers = []
    # Initialize the variable i to handle the loop.
    i = 2
    while len(prime_numbers) < n:
        # Check if the number is prime and less than n.
        if is_prime(i) and i < n:
            prime_numbers.append(i)
            # Increment i for the next iteration.
            i += 1
    return prime_numbers
def is_prime(num):
    # Check if num is less than or equal to 1, which is not prime.
    if num <= 1:
        return False
    # Check if num is 2 or 3, which are prime numbers.
    if num <= 3:
        return True
    # Check if num is even, which means it is not prime.
    if num % 2 == 0:
        return False
    # Check if num is divisible by odd numbers up to the square root of num.
    sqrt_num = int(num ** 0.5) + 1
    for i in range(3, sqrt_num, 2):
        if num % i == 0:
            return False
    # If no divisors are found, num is prime.
    return True