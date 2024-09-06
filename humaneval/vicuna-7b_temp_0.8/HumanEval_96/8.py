
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
    # this is an example of using recursion, you can use while loop and stack also
    if n == 0:
        return []
    if n == 1:
        return [2]
    # this is the base case of the recursion, when n is less than 2 it will not call itself
    # so it will directly return the array of first two prime numbers
    # if n is odd, it will not be prime number
    # if n is even, it will be a prime number
    # in this case it will be called only when n is greater than 2
    # so it will not be called when n is less than 2
    # this is the recursive call for the next number which is n+1
    # this will be called only when n is not prime
    # so it will be called only when n is even
    # so it will be called only when n is greater than 2
    # this is the recursive call for the next number which is n+1
    # this will be called only when n is not prime
    # so it will be called only when n is even
    # so it will be called only when n is greater than 2
    # this is the recursive call for the next number which is n+1
    # this will be called only when n is not prime
    # so it will be called only when n is even
    # so it will be called only when n is greater than 2
    # this is the recursive call for the next number which is n+1
    # this will be called only when n is not prime
    # so it will be called only when n is even
    # so it will be called only when n is greater than 2
    # this is the recursive call for the next number which is n+1
    # this will be called only when n is not prime
    # so it will be called only when n is even
    # so it will be called only when n is greater than 2
    # this is the recursive call for the next number which is n+1
    # this will be called only when n is not prime
    # so it will be called only when n is even
    # so it will be called only when n is greater than 2
    # this is the recursive call for the next number which
