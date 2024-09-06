def count_up_to(n):
    # check if n is 0 or 1, in that case return an empty list
    if n < 2:
        return []
    # initialize a list to store the prime numbers and an iterator
    primes = []
    iterator = 2
    while len(primes) < n:
        # iterate through integers 2 and higher
        iterator += 1
        # loop through odd and even integers, checking for divisibility
        for i in range(2, int(iterator ** 0.5) + 1):
            if iterator % i == 0:
                break
        # if the loop exits without finding a divisor, the number is prime
        else:
            primes.append(iterator)
            # update n with the remaining count of primes needed
            n -= 1
    return primes