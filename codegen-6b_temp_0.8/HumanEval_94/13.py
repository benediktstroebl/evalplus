

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
    max_prime_value = 0
    nums = []
    for i in lst:
        while i > 1:
            if i % 2 == 0:
                i /= 2
            elif i % 3 == 0:
                i /= 3
            elif i % 5 == 0:
                i /= 5
            elif i % 7 == 0:
                i /= 7
            elif i % 11 == 0:
                i /= 11
            elif i % 13 == 0:
                i /= 13
            elif i % 17 == 0:
                i /= 17
            elif i % 19 == 0:
                i /= 19
            elif i % 23 == 0:
                i /= 23
            elif i % 29 == 0:
                i /= 29
            elif i % 31 == 0:
                i /= 31
            elif i % 37 == 0:
                i /= 37
            elif i % 41 == 0:
                i /= 41
            elif i % 43 == 0:
                i /= 43
            elif i % 47 == 0:
                i /= 47
            elif i % 71 == 0:
                i /= 71
            elif i % 79 == 0:
                i /= 79
            elif i % 97 == 0:
                i /= 97
            elif i % 101 == 0:
                i /= 101
            elif i % 103 == 0:
                i /= 103
            elif i % 107 == 0:
                i /= 107
            elif i % 109 == 0:
                i /= 109
            elif i % 113 == 0:
                i /= 113
            elif i % 127 == 0:
                i /= 127
            elif i % 131 == 0:
                i /= 131
            elif i % 137 == 0:
                i /= 137
            elif i % 139 == 0:
                i /= 139
            elif i % 149 == 0:
                i /= 149
            elif i % 151 == 0:
                i /= 151
            elif i % 157 == 0:
                i /= 157
            elif