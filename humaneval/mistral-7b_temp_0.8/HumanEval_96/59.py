
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
    # Define a list to hold the prime numbers and their multiples
    prime_numbers = []

    # Define a loop to iterate through the numbers from 2 to n
    for num in range(2, n+1):
        # Check if the number is prime or not
        if is_prime(num):
            # If the number is prime, add it to the list of prime numbers
            prime_numbers.append(num)

    # Return the list of prime numbers
    return prime_numbers

