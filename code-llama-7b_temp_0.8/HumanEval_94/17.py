

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
    # if the number is 10 or less, return 1
    # iterate through lst, if the number is less than 10, add to new list
    # else:
    #   iterate through the number, if any number is less than 2, return 0
    #   else return the sum of the digits
    # return the largest prime value (from the new list)
    # print(lst)
    lst2 = [i for i in lst if i >= 10]
    lst3 = []
    for num in lst2:
        x = 1
        for i in range(2, num):
            if (num % i == 0):
                x = 0
        if (x == 1):
            lst3.append(num)
    lst3.sort()
    # print(lst3)
    # print(lst3[-1])
    x = 1
    for i in range(2, lst3[-1]):
        if (lst3[-1] % i == 0):
            x = 0
    if (x == 1):
        return lst3[-1]
    else:
        return 0





