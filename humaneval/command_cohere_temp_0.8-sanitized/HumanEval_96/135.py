def count_up_to(n):
    # check if n is 0 or 1, if so, return an empty list
    if n <= 1:
        return []
    # Initialize a list to store the prime numbers and count variable
    prime_numbers = []
    count = 0
    # Iterate through integers 2 through n
    for num in range(2, n + 1):
        # Check for prime-ness and if less than n
        if is_prime(num) and num < n:
            prime_numbers.append(num)
            count += 1
        # Stop counting if we've found n prime numbers
        if count == n:
            break
    # Return the prime numbers list
    return prime_numbers
def is_prime(n):
    # Check if n is less than or equal to 1, if so, return False
    if n <= 1:
        return False
    # Check if n is less than or equal to 3, if so, return True
    if n <= 3:
        return True
    # Check if the number is divisible by 2 or 3, if so, return False
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    # Iterate through numbers of the form 6n +(-) 1
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    # If no factors are found, return True
    return True