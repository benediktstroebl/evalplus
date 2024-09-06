
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
    arr = []
    for i in range(1, n + 1):
        if i == 2:
            count += 1
            continue
        for j in range(i + 1, n + 1):
            if is_prime(j):
                count += 1
            else:
                break
    if count!= 0:
        arr.append(count)
    return arr






