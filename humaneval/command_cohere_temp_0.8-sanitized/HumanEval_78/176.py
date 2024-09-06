def is_prime(n):
    """Checks if a number is a prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    # your code here
    count = 0
    num = str(num)
    # Iterate through each digit and check if it is a prime
    for digit in num:
        if digit in '2 3 5 7 B D':  # Manually specify prime digits
            count += 1
        elif is_prime(int(digit, 16)):  # Check if the digit in hexadecimal is prime
            count += 1
    return count