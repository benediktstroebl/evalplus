
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
    def sieve(m):
        # use python's built-in sieve function to find prime numbers less than m
        sieve = [True for i in range(1000000)]
        sieve[0] = sieve[1] = False
        sieve[2] = sieve[3] = True
        for i in range(4, int(m**0.5)-2):
            sieve[i] = (sieve[i-1] * (i+1) > m)
        for i in range(m-1000000, -1, -1):
            if sieve[i]:
                for j in range(i+1, m-1, i+1):
                    if sieve[j]:
                        sieve[j] = False
        return sieve

    def count(m):
        count = []
        for num in range(m):
            while True:
                for i in range(m):
                    if (m%i == 0):
                        break
                if sieve[num] == True:
                    count.append(num)
                    break
            if sieve[num] == False:
                break
        return count
    return count(n)
