
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
    primes = set([2, 3, 5, 7])
    if n < 3:
        return []
    elif n == 3:
        return [3]
    elif n == 4:
        return [2, 3]
    else:
        numbers = [x for x in range(2, n)]
        i = 0
        while i < len(numbers):
            if numbers[i] in primes:
                i += 1
            else:
                numbers[i] = 0
        return [x for x in numbers if x != 0]
