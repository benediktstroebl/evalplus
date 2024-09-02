
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
    # check for 0
    if n == 0:
        return []
    
    # check for 1
    if n == 1:
        return []
    
    # check for odd number
    if not n % 2:
        return []
    
    # initialize array
    result = []
    
    # for i from 2 to n
    for i in range(2, n+1):
        # check if i is prime
        if is_prime(i):
            result.append(i)
    
    return result
