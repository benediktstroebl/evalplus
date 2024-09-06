

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
    maxi = max(lst)
    if maxi == 0:
        return 0
    else:
        while maxi != 1:
            maxi //= 2
            if maxi % 2 == 0:
                continue
            else:
                break
        if maxi % 10 == 0:
            maxi //= 10
            while maxi != 1:
                maxi //= 2
                if maxi % 2 == 0:
                    continue
                else:
                    break
            if maxi % 10 == 0:
                maxi //= 10
                while maxi != 1:
                    maxi //= 2
                    if maxi % 2 == 0:
                        continue
                    else:
                        break
            return sum(str(maxi))
        else:
            return sum(str(maxi))

