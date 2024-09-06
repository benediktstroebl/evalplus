def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Handle the case of n being a power of 2, which has no digits after the decimal point.
    if n == 2:
        return 2
    while n % 2 == 0:
        n //= 2
    # Convert n into a string to access its digits.
    base = str(n)
    # Iterate through each digit, starting from the last.
    for i in range(len(base) - 1, -1, -1):
        # Check if the digit is prime.
        if all(base[i] != j for j in range(2, int(base[i]) + 1, 1)):
            return int(base[i])
        # If not, divide n by the digit.
        n //= int(base[i])
    return 1