
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
    primeList = []
    n1 = 0
    while n1 < n:
        n1 += 1
        prime = True
        for num in range(2,n1):
            if n1 % num == 0:
                prime = False
                break
            if prime:
                primeList.append(n1)
    return primeList
