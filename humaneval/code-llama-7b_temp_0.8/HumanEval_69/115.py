
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
    ans = -1
    if len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        if lst[0] > 0 and lst[1] > 0:
            if lst[0] >= lst[1]:
                return lst[0]
            else:
                return lst[1]
        else:
            return -1
    else:
        for item in lst:
            if item > 0:
                if lst.count(item) >= item:
                    if ans < item:
                        ans = item
        return ans
