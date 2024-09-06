

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
    prime = [1 for i in range(31)]
    prime[0] = 0
    prime[1] = 0
    prime[2] = 0
    for i in range(31):
        for j in range(31):
            if prime[i] == 1 and prime[j] == 1:
                if i + j < 31:
                    prime[i + j] = 0
                if 2 * i < 31:
                    prime[2 * i] = 0
                if 3 * j < 31:
                    prime[3 * j] = 0
    for i in range(len(lst)):
        if lst[i] == 0:
            lst[i] = 1
    ans = 0
    for i in range(len(lst)):
        if prime[lst[i]] == 1:
            ans += lst[i]
    return sum(str(ans))

