
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
    # initialize a list to store the prime numbers
    prime_numbers = []
    # check if n is 0
    if n == 0:
        return []
    # check if n is prime
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            # check if n is divisible by i
            if not n % i:
                break
        else:
            # if n is not divisible by any integer from 2 to n/2, it is a prime number
            prime_numbers.append(n)
    # add the previous prime numbers to the list and start again
    while len(prime_numbers) < n:
        for i in range(2, int(n**0.5) + 1):
            # check if n is divisible by i
            if not n % i:
                break
        else:
            # if n is not divisible by any integer from 2 to n/2, it is a prime number
            prime_numbers.append(n)
    return prime_numbers