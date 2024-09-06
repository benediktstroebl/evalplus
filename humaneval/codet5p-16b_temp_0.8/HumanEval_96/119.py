
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

    if n <= 0:
        return []
    elif n == 1:
        return []
    elif n == 2:
        return [2]
    elif n == 3:
        return [2,3]
    else:
        list_of_primes = [2,3]
        for i in range(5,n+1):
            prime = True
            for prime_number in list_of_primes:
                if prime_number > math.sqrt(i):
                    break
                elif i % prime_number == 0:
                    prime = False
                    break
            if prime:
                list_of_primes.append(i)
        return list_of_primes



