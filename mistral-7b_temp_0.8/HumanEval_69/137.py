
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
    #The code below does not work
    temp=[]
    for i in lst:
        if i in lst:
            lst.remove(i)
            temp.append(i)

    #print(temp)
    #print(lst)

    #max_value=max(temp)
    #print(temp)
    #print(max_value)

    for i in temp:
        if max(lst)>i:
            max_value=max(lst)
            break

    print(max_value)

    if max_value==-1:
        return -1
    else:
        return max_value
