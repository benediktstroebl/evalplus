

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
    # ======== First solution, took a minute and failed ========
    # max_value = max(lst)
    # temp = 0
    # for i in range(len(str(max_value))):
    #     temp += int(str(max_value)[i])
    # return temp

    # ======== Second solution, took 22 minutes to complete ========
    # max_value = max(lst)
    # sum_digits = []
    # while max_value > 0:
    #     sum_digits.append(max_value % 10)
    #     max_value //= 10
    # return sum(sum_digits)

    # ======== Third solution, took 4 minutes, definitely faster than 80% ========
    max_value = max(lst)
    sum_digits = 0
    while max_value > 0:
        sum_digits += max_value % 10
        max_value //= 10
    return sum_digits

