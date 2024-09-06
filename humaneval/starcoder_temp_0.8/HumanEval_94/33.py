

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
    l = []
    for x in lst:
        l.append(x)
    for i in range(len(l)):
        if (l[i] < 2):
            l[i] = 2
        elif (l[i] == 2):
            l[i] = 3
        elif (l[i] > 2 and l[i] % 2 == 0):
            l[i] = 3
        elif (l[i] > 2 and l[i] % 2!= 0):
            l[i] = 5

    l2 = []
    for x in l:
        l2.append(x)
    for i in range(len(l2)):
        if (l2[i] < 2):
            l2[i] = 2
        elif (l2[i] == 2):
            l2[i] = 3
        elif (l2[i] > 2 and l2[i] % 2 == 0):
            l2[i] = 3
        elif (l2[i] > 2 and l2[i] % 2!= 0):
            l2[i] = 5

    l3 = []
    for x in l2:
        l3.append(x)
    for i in range(len(l3)):
        if (l3[i] < 2):
            l3[i] = 2
        elif (l3[i] == 2):
            l3[i] = 3
        elif (l3[i] > 2 and l3[i] % 2 == 0):
            l3[i] = 3
        elif (l3[i] > 2 and l3[i] % 2!= 0):
            l3[i] = 5

    return sum(l3)
