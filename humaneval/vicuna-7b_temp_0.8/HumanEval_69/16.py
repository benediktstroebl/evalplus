
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
    # sort the list
    lst = sorted(lst)
    
    # find the first element that has frequency greater than itself
    i = 0
    while i < len(lst) and lst[i] <= lst[i]:
        i += 1
    if i == len(lst):
        return -1
    else:
        j = i + 1
        max_frequency = lst[i]
        max_value = lst[i]
        while j < len(lst):
            if lst[j] > max_value:
                max_frequency = max(max_frequency, lst[j] - lst[i])
                max_value = lst[j]
            j += 1
        return max_value
