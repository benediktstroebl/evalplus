
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
    # get a list of frequencies for each integer
    frequencies = {}
    for num in lst:
        frequencies[num] = frequencies.get(num, 0) + 1
    
    max_num = -1
    max_frequency = -1
    for num in frequencies.keys():
        if frequencies[num] > max_frequency and num > 0:
            max_num = num
            max_frequency = frequencies[num]
    return max_num
    
