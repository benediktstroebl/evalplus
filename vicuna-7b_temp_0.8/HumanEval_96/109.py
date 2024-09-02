
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
    # check for 0 case
    if n == 0:
        return []
    
    # check for 1 case
    if n == 1:
        return []
    
    # check for 2 case
    if n == 2:
        return [2]
    
    # check for other cases
    # check if n is prime and less than n
    # if so, return [n]
    # if not, recursively call with n-1
    # if n is prime, call with n-1 and increment the count of n
    # if n is not prime, call with n-1 and increment the count of n
    # return the count of n
    count = []
    for i in range(2,int(n)+1):
        if n % i == 0:
            break
        if n % i == 1:
            count.append(n)
        else:
            count.append(count[-1]+1)
    return count
