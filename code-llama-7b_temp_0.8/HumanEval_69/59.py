
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
    if lst == [] or lst[0] < 0:
        return -1
    m = lst[0]
    m_freq = 0
    for x in lst:
        if x > 0:
            freq = lst.count(x)
            if freq > m_freq or (freq == m_freq and x > m):
                m = x
                m_freq = freq
    if m_freq >= m:
        return m
    else:
        return -1

