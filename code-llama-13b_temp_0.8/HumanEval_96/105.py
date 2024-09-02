
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
    count = 0
    list = []
    i = 2
    while count < n:
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime:
            if i < n:
                list.append(i)
            count += 1
        i += 1
    return list
