
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

    # We can not use the built in prime number function, so let's implement our own
    # since we need to check all the numbers before n to see if they are prime, we can use a list to store them
    primes = []
    # Initialize a list with the first n numbers, which are 1,2,3,4,...,n-1
    numbers = list(range(n))
    for number in numbers:
        # If the number in the list is prime, we can append it to the primes list
        # We can add the list we are checking to the primes list if it is prime
        if prime(number) == True:
            primes.append(number)
    return primes
