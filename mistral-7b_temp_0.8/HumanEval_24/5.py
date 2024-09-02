

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    # answer = 1
    # for i in range(2, n+1):
    #     if n % i == 0:
    #         answer = i
    #     return answer

    #return 1

    answer = 1
    for i in range(2, n+1):
        if n % i == 0:
            answer = i

    return answer

