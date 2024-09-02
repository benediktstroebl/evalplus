
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
    # Use a hash set to store the primes found so far
    # Use a queue to keep track of the remaining numbers
    primes = set()
    while True:
        # Remove the first prime from the queue
        prime = primes.pop()
        # Add the current number to the set of primes
        primes.add(prime)
        # Add the current number to the list of results
        results.append(prime)
        # If the current number is greater than the next prime, break the loop
        if prime <= n:
            break
    return results