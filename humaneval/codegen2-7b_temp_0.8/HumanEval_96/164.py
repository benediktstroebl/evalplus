
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
    count = []
    if n == 0:
        return count
    if n == 1:
        return count

    for x in range(2, n+1):
        i = 0
        while i < len(count):
            if x % count[i] == 0:
                i = -1
            else:
                i += 1
        count.append(x)
    return count

