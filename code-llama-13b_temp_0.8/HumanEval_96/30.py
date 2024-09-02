
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
    # Your code here
    # a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    # b = a[:n]

    # for i in b:
    #     if i <= 1:
    #         b.remove(i)
    #     else:
    #         for j in range(2,i):
    #             if (i % j) == 0:
    #                 b.remove(i)
    #                 break
    
    # return b

    primes = []
    i = 2

    while i <= n:
        if i <= 1:
            i += 1
        else:
            for j in range(2,i):
                if (i % j) == 0:
                    i += 1
                    break
            else:
                primes.append(i)
                i += 1

    return primes
