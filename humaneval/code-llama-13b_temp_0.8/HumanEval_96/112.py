
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

    # A list of prime numbers
    prime_list = []

    # Loop through all the numbers up to n
    for i in range(n + 1):

        # If the number is less than 2, break out of the loop
        if i < 2:
            break

        # Check to see if the number is prime
        # if yes add to the prime list
        elif i <= n and is_prime(i):
            prime_list.append(i)

    # return the list of primes
    return prime_list

