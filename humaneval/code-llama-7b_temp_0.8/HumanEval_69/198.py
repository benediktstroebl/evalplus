
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

    def get_freq(lst, val):
        return lst.count(val)
    
    def get_greatest(lst, val):
        if val == -1:
            return -1
        if val in lst:
            return val
    
    def get_element_max_freq(lst):
        max_freq = -1
        max_value = -1
        for val in lst:
            if max_freq < get_freq(lst, val):
                max_freq = get_freq(lst, val)
                max_value = val
        return max_value
    
    max_value = get_element_max_freq(lst)
    return get_greatest(lst, max_value)

