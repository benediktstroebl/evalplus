
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

    #print(lst)
    x = lst[0]
    for i in lst:
        if i > x:
            if lst.count(i) >= i:
                x = i
                #print(x)
            else:
                x = lst[0]
        elif i == x and lst.count(i) >= x:
            x = i
        else:
            x = lst[0]
    #print(x)
    if x == lst[0]:
        return -1
    else:
        return x
