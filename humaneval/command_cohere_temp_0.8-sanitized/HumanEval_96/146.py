def count_up_to(n):
    """Implementation for the function that generates prime numbers up to 'n'."""
    # Create a list to store prime numbers less than 'n'
    prime_numbers = []
    # Counter for loop
    c = 2 # Integer to start with
    # Loop through numbers less than 'n'
    while c < n:
        # Loop through 2, 3, 5, 7, 11, 13, 17, 19, 21, 23, 29, 31, 37 
        # ... until the number is less than or equal to n
        for x in range(2, int(n**0.5) + 1):
            if c % x != 0 and c != x:
                break
            elif c == x:
                prime_numbers.append(c)
        c += 1 
    # Return the prime_numbers list
    return prime_numbers