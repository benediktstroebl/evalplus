def count_up_to(n):
    # check if n is 0 or 1, if so, return an empty list
    if n == 0 or n == 1:
        return []
    # Create a list to store the first n prime numbers less than n
    count_up = []
    # Start from the second integer (skipping 1 as it is not a prime number)
    i = 2
    while len(count_up) < n:
        # Check if the current integer is prime
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        # If the current integer is prime, add it to the list
        if is_prime:
            count_up.append(i)
        i += 1
    # Return the list of prime numbers
    return count_up