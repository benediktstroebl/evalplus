
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
    if n < 1:
        return []
    a = [2,3]
    if n < 3:
        return a
    for i in range(3,n+1):
        is_prime = True
        for x in range(2,i//2+1):
            if i%x == 0:
                is_prime = False
                break
        if is_prime:
            a.append(i)
    return a
