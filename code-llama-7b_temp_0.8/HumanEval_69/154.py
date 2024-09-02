
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
    if not lst: return -1

    # finding the highest number in lst
    highest = max(lst)

    # initializing a dictionary which will help us to count the freq of each element
    freq_dict = dict()

    # initializing the freq of highest as 1
    freq_dict[highest] = 1

    # populating the freq of highest 
    for val in lst:
        if val == highest:
            freq_dict[val] += 1

    # finding the max freq of the list
    max_freq = max(freq_dict.values())

    # for each freq, check if the freq >= highest, if yes then return the freq
    for k in freq_dict.keys():
        if freq_dict[k] >= max_freq and k > 0:
            return k

    return -1
