

def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """
    new_lst = []
    for el in lst:
        if el % 2!= 0:
            new_lst.append(el)

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n % 3 == 0:
            return False
        r = int(n ** 0.5)
        f = 5
        while f <= r:
            # print('\t', f)
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True

    def sum_digits(n):
        if n < 10:
            return n
        else:
            return n % 10 + sum_digits(n // 10)

    max_prime = 0
    for el in new_lst:
        if is_prime(el):
            if el > max_prime:
                max_prime = el

    return sum_digits(max_prime)
