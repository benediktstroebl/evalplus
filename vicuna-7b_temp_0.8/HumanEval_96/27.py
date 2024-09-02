
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
    # Create a dictionary that maps each prime number to its count
    prime_count = {}
    for num in primes:
        prime_count[num] = prime_count.get(num, 0) + 1

    # Initialize a list that will store the first n integers that are prime numbers and less than n
    result = []

    # Iterate through the range 2 to n-1
    for num in range(2, n):
        # Check if num is prime
        if num in prime_count:
            # If it is prime, add it to the result list
            result.append(num)

    # Return the result list
    return result
