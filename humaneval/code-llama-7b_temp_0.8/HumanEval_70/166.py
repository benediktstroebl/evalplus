
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    #Base Case
    if len(lst) == 0:
        return []
    #Recursive Case
    else:
        #Find Minimum Value
        minValue = min(lst)
        #Find Maximum Value
        maxValue = max(lst)
        #Split Input List on Minimum Value
        lstLeft = []
        lstRight = []
        for i in lst:
            if i == minValue:
                lstLeft.append(i)
            if i == maxValue:
                lstRight.append(i)
            if i != minValue and i != maxValue:
                lstRight.append(i)
        #Add Minimum Value to Left List
        lstLeft.append(minValue)
        #Recurse on Left and Right List
        return strange_sort_list(lstLeft) + [maxValue] + strange_sort_list(lstRight)
    
