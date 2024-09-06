
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
    # IMPLEMENT YOUR SOLUTION HERE
    # dict_freqs = {i: lst.count(i) for i in lst}
    # new_lst = []
    # for i in dict_freqs.keys():
    #     if dict_freqs[i] >= i:
    #         new_lst.append(i)
    # return max(new_lst) if len(new_lst) > 0 else -1
    lst_freqs = [lst.count(i) for i in lst]
    return max([i for i in lst if lst_freqs[lst.index(i)] >= i]) if len([i for i in lst if lst_freqs[lst.index(i)] >= i]) else -1

