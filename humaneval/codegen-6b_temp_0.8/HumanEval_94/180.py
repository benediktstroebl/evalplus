

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
    lst2 = [str(i) for i in lst]
    print(lst2)

    # https://en.wikipedia.org/wiki/Prime_number#Random_sample_method
    # http://mathworld.wolfram.com/PrimeNumber.html
    # http://mathworld.wolfram.com/PrimeCountingFunction.html
    # https://en.wikipedia.org/wiki/Fermat_factorization
    # http://mathworld.wolfram.com/FermatFactors.html

    dct = {}
    for i in lst2:
        if len(i) == 1:
            dct[int(i)] = 1
        elif len(i) == 2:
            dct[int(i)] = 2
        elif len(i) == 3:
            dct[int(i)] = 4
        elif len(i) == 4:
            dct[int(i)] = 7
        elif len(i) == 5:
            dct[int(i)] = 13
        elif len(i) == 6:
            dct[int(i)] = 19
        elif len(i) == 7:
            dct[int(i)] = 29
        elif len(i) == 8:
            dct[int(i)] = 37
        elif len(i) == 9:
            dct[int(i)] = 41
        elif len(i) == 10:
            dct[int(i)] = 47
        elif len(i) == 11:
            dct[int(i)] = 53
        elif len(i) == 12:
            dct[int(i)] = 59
        elif len(i) == 13:
            dct[int(i)] = 67
        elif len(i) == 14:
            dct[int(i)] = 71
        elif len(i) == 15:
            dct[int(i)] = 79
        elif len(i) == 16:
            dct[int(i)] = 89
        elif len(i) == 17:
            dct[int(i)] = 97
        elif len