
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
    counter = {}
    for i in lst:
        if i not in counter.keys():
            counter[i] = 1
        else:
            counter[i] += 1
    print(counter)
    # for i in counter.keys():
    #     if i > 0 and counter[i] >= i:
    #         print(i)
    #         return i
    # return -1
    return max(k for k in counter.keys() & {k for k in counter.values() if k >= k} & {k for k in lst if k > 0})
