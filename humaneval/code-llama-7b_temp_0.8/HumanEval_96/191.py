
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

    # create an empty list to append to
    list_of_primes = []

    # check every integer in the range, to see if it is a prime
    # iterate over list of numbers between 1 and n
    for i in range(1,n+1):
        # iterate over the list of numbers between 1 and i
        for j in range(1, i+1):
            # if i divided by j does not leave a remainder
            if i % j == 0:
                # if j is equal to itself, add it to the list of primes
                if j == i:
                    list_of_primes.append(j)
                # else, it is not a prime and do not add it to the list
                else:
                    break
        # check to see if the integer is a prime, if it is, add it to the list
        else:
            if i != 1:
                list_of_primes.append(i)

    return list_of_primes
