
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
    # Return empty list if n is 0
    if n == 0:
        return []

    # Return empty list if n is negative
    if n < 0:
        return []

    # Initialize a list to contain prime numbers
    prime_numbers = []

    # Loop from 2 to n
    for number in range(2, n+1):
        # Check if number is prime
        if is_prime(number):
            # Append number to prime_numbers list
            prime_numbers.append(number)

    # Return the list
    return prime_numbers
