
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
    numbers = [True for _ in range(n)]
    numbers[0] = False
    numbers[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if numbers[i]:
            for j in range(i * i, n, i):
                numbers[j] = False
    return [x for x in range(2, n) if numbers[x]]
