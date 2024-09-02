
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
    # 1. if there is no element in list, return -1
    # 2. find the max element in list and count the number of this element
    # 3. return the element if its count >= max element
    # 4. else return -1
    if len(lst) == 0:
        return -1
    else:
        max_num = max(lst)
        count = 0
        for i in range(len(lst)):
            if lst[i] == max_num:
                count += 1
            if count >= max_num:
                return max_num
        return -1
    
