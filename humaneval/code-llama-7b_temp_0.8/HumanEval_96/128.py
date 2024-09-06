
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
    # A dictionary to store primes
    prime_numbers = {}
    primes = []

    # A checker function to see if a number is prime or not.
    def check_if_prime(n):
        for i in prime_numbers:
            if (n % i == 0) and (i != n):
                return False
        return True

    # Traverse from 0 to n and put all prime numbers in the dictionary
    for i in range(0, n+1):
        if check_if_prime(i):
            prime_numbers[i] = True

    # Traverse the dictionary and get all prime numbers into the result array
    for i in range(0, n+1):
        if i in prime_numbers:
            primes.append(i)

    return primes

