
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
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    if freq_dict[0] >= 1:
        return 0
    else:
        for i in range(len(lst) - 1, 0, -1):
            if lst[i] > lst[i - 1]:
                if lst[i] - lst[i - 1] >= 2:
                    return lst[i] - 1
                elif lst[i] - lst[i - 1] == 1 and freq_dict[lst[i]] >= 2:
                    return lst[i]
    return -1
