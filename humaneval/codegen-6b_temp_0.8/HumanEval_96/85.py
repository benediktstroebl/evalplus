
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
    if n <= 1:
        return []
    max_divisor = n // 2 + 1
    primes = [2]
    upto = 3
    while upto < n:
        upto_sqrt = upto ** 2
        divisor = 3
        while divisor <= max_divisor:
            if upto_sqrt % divisor == 0:
                break
            divisor += 2
        if divisor > max_divisor:
            primes.append(upto)
        upto += 2
    return primes
        

