
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
    freq_lst = [(0, [])]
    for num in lst:
        if len(freq_lst) == 0 or freq_lst[0][1] < num:
            freq_lst = [(freq, [num])]
        else:
            freq_lst[-1][1].append(num)
            freq_lst.pop()
    return freq_lst[-1][0]

lst = [1, 2, 2, 3, 1]
