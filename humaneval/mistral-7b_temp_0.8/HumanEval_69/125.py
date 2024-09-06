
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
    freq={}
    max_elem=lst[0]
    max_freq=1
    for i in lst:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
        if freq[i]>max_freq:
            max_elem=i
            max_freq=freq[i]
    return max_elem if max_freq>=max_elem else -1
