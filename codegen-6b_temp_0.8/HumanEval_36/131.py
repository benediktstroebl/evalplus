

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    "*** YOUR CODE HERE ***"
    #The following implementaion is the most naive implementation
    #It takes too long to run
    #res = 0
    #for i in range(n):
    #    if i % 11 == 0 or i % 13 == 0:
    #        res += 1
    #return res

    #The following implementation is faster and shorter
    return sum([1 for i in range(n) if i % 11 == 0 or i % 13 == 0])
