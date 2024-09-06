from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    # initialize result list
    result = []
    # initialize variable for counting times of factor
    count = 1
    # iterate through all digits of the number
    for digit in str(n):
        # if it's digit 0, it means the number is even
        if digit == '0':
            # if it's even, it can't be factorized
            if n % 2 == 0:
                result.append(1)
                count += 1
            else:
                result.append(2)
                count += 1
        else:
            # if it's digit 1, it means the number is odd
            if n % 2 == 1:
                # if it's odd, it can be factorized
                if n > 1:
                    result.append(count)
                    count += 1
                    # check for divisibility by 2
                    if n % 2 == 0:
                        result.append(1)
                    # check for divisibility by 3
                    if n % 3 == 0:
                        result.append(1)
                    # check for divisibility by 4
                    if n % 4 == 0:
                        result.append(1)
                    # check for divisibility by 5
                    if n % 5 == 0:
                        result.append(1)
                    # check for divisibility by 6
                    if n % 6 == 0:
                        result.append(1)
                    # check for divisibility by 7
                    if n % 7 == 0:
                        result.append(1)
                    # check for divisibility by 8
                    if n % 8 == 0:
                        result.append(1)
                    # check for divisibility by 9
                    if n % 9 == 0:
                        result.append(1)
                    # check for divisibility by 10
                    if n % 10 == 0:
                        result.append(1)
                    # check for divisibility by 11
                    if n % 11 == 
