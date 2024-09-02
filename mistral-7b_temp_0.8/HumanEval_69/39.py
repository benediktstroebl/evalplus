
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
    x = sorted(lst)
    f = []
    f.append(x.count(x[0]))
    for i in range(1, len(x)):
        if x[i] == x[i-1]:
            f.append(f[i-1])
        else:
            f.append(x.count(x[i]))
    for i in range(len(f)):
        if f[i] >= x[i]:
            return x[i]
    return -1


