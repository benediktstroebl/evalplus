
def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """
    # Create a list to store the prime numbers
    prime_numbers = []
    # Create a variable to store the next prime number
    next_prime_num = 2
    # Iterate through the numbers starting from 2
    for i in range(2, n+1):
        # Check if the current number is prime
        if not is_prime(i):
            continue
        # If it is prime, add it to the list
        prime_numbers.append(i)
        # Update the variable to store the next prime number
        next_prime_num = i + 1
    return prime_numbers
