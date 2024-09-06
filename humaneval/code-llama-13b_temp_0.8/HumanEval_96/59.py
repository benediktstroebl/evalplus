
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
    # return [x for x in range(2, n + 1) if is_prime(x)]
    # return list(filter(lambda x: is_prime(x), range(2, n + 1)))
    # if n < 2:
    #     return []
    # result = [2]
    # for x in range(3, n, 2):
    #     for i in range(2, int(x**0.5)+1):
    #         if x % i == 0:
    #             break
    #     else:
    #         result.append(x)
    # return result
    result = []
    if n <= 2:
        return result
    result.append(2)
    for x in range(3, n, 2):
        if is_prime(x):
            result.append(x)
    return result

