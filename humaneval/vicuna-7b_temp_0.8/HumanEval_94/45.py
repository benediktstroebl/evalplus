

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
    lst = sorted(lst)
    if lst[0] == 0:
        return 0
    for i in range(1, len(lst)):
        for j in range(i, len(lst)):
            if lst[i] * lst[j] == lst[j] + lst[i]:
                lst.remove(lst[i])
                return 0
    return 1

lst = [3,3,4,5,6,6,6,7,8,8,9,9,10,10,10,11,12,13,13,13,14,14,15,15,16,16,16,17,17,18,18,18,18,19,19,20,20,20,21,21,22,22,22,23,23,23,23,23,24,24,24,25,25,25,25,26,26,26,26,26,27,27,27,27,27,27,28,28,28,28,28,29,29,29,29,29,30,30,30,30,30,30,31,31,31,31,31,31,31,31,32,32,32,32,32,32,32,32,33,33,33,33,33,33,33,33,34,34,34,34,34,34,34,34,34,34,34,34,35,35,35,35,35,35,35,35,35,35,35,36,36,36,36,36,36,36,36,36,36,36,36,36,36
