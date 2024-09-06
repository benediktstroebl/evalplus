def count_up_to(n):
    # Initialize an empty list to store the prime numbers
    result = []
    # Iterate from 2 to n, and loop only if the current number is prime
    for num in range(2, n + 1):
        # Check if the current number is prime, and if so, add it to the result list
        if is_prime(num):
            result.append(num)
            # If the desired number of primes has been reached, break the loop
            if len(result) == n:
                break
    return result
def is_prime(n):
    """
    Checks whether a number is prime or not.

    Args:
        n (int): Number to be checked.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True