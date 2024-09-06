
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    lst.sort()
    # max = len(lst)
    # for i in range(len(lst)-1, -1, -1):
    #     if lst[i] == lst[i-1]:
    #         continue
    #     else:
    #         max = i
    #         break
    # print(max)
    # if max == 0:
    #     return -1
    # else:
    #     print(lst[max])
    #     return lst[max]
    if lst[0] == 0:
        return -1
    for val in range(len(lst)-1, -1, -1):
        if val == len(lst):
            return -1
        else:
            if lst[val] == lst[val-1]:
                continue
            else:
                if lst[val] > lst[val-1]:
                    return lst[val-1]
                else:
                    return lst[val]

        
