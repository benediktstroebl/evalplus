
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
    # current_max_freq = 0
    # current_max_element = -1
    # element_count = {}
    # for el in lst:
    #     element_count.setdefault(el, 0)
    #     element_count[el] += 1
    #     if element_count[el] > current_max_freq and el > 0:
    #         current_max_freq = element_count[el]
    #         current_max_element = el
    # return current_max_element
    # 1 liner below
    return max([x for x in set(lst) if lst.count(x) >= x] or [-1])
