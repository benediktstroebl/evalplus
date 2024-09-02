
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
    primes = []
    if n <= 1:
        return []
    numbers = [i for i in range(2, n + 1)]
    while numbers:
        base, count = numbers[0], numbers[0]
        while count < len(numbers):
            base = numbers[count]
            numbers = [i for i in numbers[1:]]
            for i in range(2, int(base ** 0.5) + 1):
                if i < len(numbers):
                    numbers[i] = base * numbers[i]
                else:
                    break
            else:
                primes.append(base)
                count += 1
        numbers = numbers[count:]
    return primes

