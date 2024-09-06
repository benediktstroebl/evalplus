

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

    lst_copy = lst[:]

    #print(lst_copy)
    lst_copy = list(set(lst_copy))
    #print(lst_copy)
    lst_copy = sorted(lst_copy)
    #print(lst_copy)
    lst_copy.remove(0)
    #print(lst_copy)
    lst_copy.remove(1)
    #print(lst_copy)
    lst_copy.remove(2)
    #print(lst_copy)
    lst_copy.remove(3)
    #print(lst_copy)
    lst_copy.remove(4)
    #print(lst_copy)
    lst_copy.remove(5)
    #print(lst_copy)
    lst_copy.remove(6)
    #print(lst_copy)
    lst_copy.remove(7)
    #print(lst_copy)
    lst_copy.remove(8)
    #print(lst_copy)
    lst_copy.remove(9)
    #print(lst_copy)
    i = len(lst_copy)-1
    while i!= -1:
        j = i-1
        if is_prime(lst_copy[i]):
            while j!= -1:
                if lst_copy[i]%lst_copy[j] == 0:
                    del lst_copy[i]
                j -= 1
        i -= 1
    #print(lst_copy)
    return sum(lst_copy)
