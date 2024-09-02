
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
    hs=[]
    for i in lst:
        if i not in hs:
            hs.append(i)
    #print(hs)
    d={}
    for i in hs:
        d[i]=lst.count(i)
    #print(d)
    max=d[max(d.values())]
    for k in d.keys():
        if d[k]>=k:
            max=k
    #print(max)
    return max if max>=1 else -1

