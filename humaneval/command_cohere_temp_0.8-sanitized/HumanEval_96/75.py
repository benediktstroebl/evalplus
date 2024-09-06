def count_up_to(n):
    # check if n is 0 or 1, in which case return an empty list
    if n == 0 or n == 1:
        return []
    # initialize a list to store the prime numbers
    count = []
    # initialize a variable to track the number of primes found
    count_tracker = 0
    # iterate through integers from 2 to n
    for num in range(2, n + 1):
        # if num is prime, add it to the list and increment the counter
        if is_prime(num):
            count.append(num)
            count_tracker += 1
        # if the counter equals n, break the loop as enough primes have been found
        if count_tracker == n:
            break
    # return the list of primes
    return count
def is_prime(n):
    # check if n is 1, in which case it is not prime
    if n <= 1:
        return False
    # check if n is 2 or 3, in which case it is prime
    if n <= 3:
        return True
    # check if n is even, in which case it is not prime
    if n % 2 == 0:
        return False
    # check divisibility between 3 and sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    # if no divisors are found, n is prime
    return True