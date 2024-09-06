
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
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5)-1):
        for j in range(2, int(n**0.5)+1):
            if sieve[i] and sieve[j] and sieve[i]%j == 0:
                break
        else:
            sieve[i] = False
    return [i for i in range(1, int(n**0.5)+1) if sieve[i]]
