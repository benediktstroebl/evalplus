
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
    # The key idea is to use a dictionary to store the frequency of the elements
    dic = {}

    for elem in lst:
        # If the element is not in the dictionary, add the element with its frequency as 1
        if elem not in dic:
            dic[elem] = 1
        # Otherwise, increment the frequency of the element
        else:
            dic[elem] += 1

    # Iterate through the dictionary to find the element with the maximum frequency
    max_val = -1
    for key in dic.keys():
        if dic[key] > dic[max_val]:
            max_val = key

    return max_val

