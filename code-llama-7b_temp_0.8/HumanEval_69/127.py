
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
    #put the values into a dictonary to store their value
    #as well as frequency
    dic = {}
    for i in lst:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    #find the values that are greater than 0, and have a frequency greater than or equal to their value
    result = []
    for k, v in dic.items():
        if k > 0 and v >= k:
            result.append(k)
    #print(result)

    #find the max value in the list
    max_val = 0
    for i in result:
        if i > max_val:
            max_val = i
    #print(max_val)

    #if the max value is in the list, return it
    if max_val in result:
        return max_val
    #if the max value is not in the list, return -1
    else:
        return -1
