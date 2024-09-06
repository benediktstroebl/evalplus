
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
    # count_up_to(0) is empty list
    if n == 0:
        return []
    
    # create empty list for result
    result = []
    
    # loop through numbers from 2 to n
    for i in range(2, n+1):
        # check if number is prime
        if is_prime(i):
            # add number to result list
            result.append(i)
        
    # return result list
    return result
