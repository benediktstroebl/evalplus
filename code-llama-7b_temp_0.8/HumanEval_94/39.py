

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
    new_lst = lst
    new_lst = filter(None, lst)
    new_lst = [n for n in lst if n!=0]
    new_lst = filter(lambda x: x % 2 != 0, new_lst)
    new_lst = filter(lambda x: x % 3 != 0, new_lst)
    new_lst = filter(lambda x: x % 5 != 0, new_lst)
    new_lst = filter(lambda x: x % 7 != 0, new_lst)
    new_lst = filter(lambda x: x % 11 != 0, new_lst)
    new_lst = filter(lambda x: x % 13 != 0, new_lst)
    new_lst = filter(lambda x: x % 17 != 0, new_lst)
    new_lst = filter(lambda x: x % 19 != 0, new_lst)
    new_lst = filter(lambda x: x % 23 != 0, new_lst)
    new_lst = filter(lambda x: x % 29 != 0, new_lst)
    new_lst = filter(lambda x: x % 31 != 0, new_lst)
    new_lst = filter(lambda x: x % 37 != 0, new_lst)
    new_lst = filter(lambda x: x % 41 != 0, new_lst)
    new_lst = filter(lambda x: x % 43 != 0, new_lst)
    new_lst = filter(lambda x: x % 47 != 0, new_lst)
    new_lst = filter(lambda x: x % 49 != 0, new_lst)
    new_lst = filter(lambda x: x % 53 != 0, new_lst)
    new_lst = filter(lambda x: x % 59 != 0, new_lst)
    new_lst = filter(lambda x: x % 61 != 0, new_lst)
    new_lst = filter(lambda x: x % 67 != 
