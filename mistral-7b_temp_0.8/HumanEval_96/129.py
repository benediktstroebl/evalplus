
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
    #check for negative integers
    if n<0:
        return []
    #create an empty list to store prime numbers
    prime_numbers = []
    #create an iterator to count up to n
    i = 2
    while i <= n:
        #if the iterator is prime, add it to the list
        if is_prime(i):
            prime_numbers.append(i)
        #increment the iterator
        i = i + 1
    return prime_numbers
