
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
    # no need to check if n is 0 or 1, since n = 0 is neither prime nor composite
    if n == 1:
        return []
    # no need to check if n is 2, since we already know that 2 is neither prime nor composite
    elif n == 2:
        return [2]
    # if n is prime, don't need to check more since those we've already seen are either prime or
    # composite
    else:
        n_set = set([n])
        primes_to_append = [n]
        # base case when n is even (we know it is not a prime, since n - 1 is a prime)
        if n % 2:
            return primes_to_append
        # if n - 1 is prime, we know that n is not a prime, since (n-1) is not a prime
        else:
            # check if n - 1 is a prime
            if is_prime(n - 1):
                primes_to_append.append(n - 1)
            n_set.add(n - 1)
            for i in range(n, n * 2, 2):
                if i not in n_set:
                    primes_to_append.append(i)
                    n_set.add(i)
            return primes_to_append

