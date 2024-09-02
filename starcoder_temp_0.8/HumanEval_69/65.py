
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
    # Your code here
    #Create a dictionary to hold the frequency of each value
    dic = {}
    #Loop through list to find the largest value
    for i in range(len(lst)):
        if lst[i] > 0:
            if lst[i] in dic:
                dic[lst[i]] += 1
            else:
                dic[lst[i]] = 1
    #Loop through the dictionary to find the key of the value with the highest frequency
    for k, v in dic.items():
        if v >= k:
            return k
    #If no such value exists, return -1
    return -1
