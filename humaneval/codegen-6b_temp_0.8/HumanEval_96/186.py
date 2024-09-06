
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
    def _count_up_to(n):
        """
        :param n: the nth number to count
        :return: the first <n> primes
        """
        def get_primes(n):
            """
            :param n: the max number to count to
            :return: a list of all the primes up to n
            """
            primes = []
            for n in range(2, n):
                for i in range(2, n):
                    if n % i == 0:
                        break
                else:
                    primes.append(n)
            return primes
        if n < 1:
            return []
        if n == 1:
            return []
        if n == 2:
            return [2]
        if n == 3:
            return [2, 3]
        primes = get_primes(n)
        numbers = [n]
        for i in range(len(primes) - 1):
            numbers.append(primes[i] + primes[-1])
        numbers.extend(primes)
        return numbers[:n]
    if n < 1:
        return []
    if n == 1:
        return []
    if n == 2:
        return [2]
    if n == 3:
        return [2, 3]
    return _count_up_to(n)
count_up_to(1)