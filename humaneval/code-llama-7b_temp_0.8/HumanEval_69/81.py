
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
    #leetcode solution
    if not lst:
        return -1

    freq = {}
    for i in lst:
        freq[i] = freq.get(i, 0) + 1

    m = max(freq.values())
    for k in freq:
        if freq[k] >= k and m <= k:
            return k

    return -1

    # IDEA:
    # make a dictionary of the frequencies
    # find the max value in that dictionary
    # for each value in that dictionary check if it is greater than or equal to it's key
    # if it is, return the value

    # freq = {}
    # for i in lst:
    #     freq[i] = freq.get(i, 0) + 1
    # print(freq)

    # m = max(freq.values())
    # print(m)

    # for k in freq:
    #     if freq[k] >= k and m <= k:
    #         return k

    # return -1


    # EXAMPLES:
    # search([4, 1, 2, 2, 3, 1]) == 2
    # freq = {1: 2, 2: 2, 3: 1, 4: 1}
    # max(freq.values) = 2
    # if k in freq and freq[k] >= k and m <= k:
    #     return k
    # return -1

    # search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
    # freq = {1: 1, 2: 2, 3: 3, 4: 3}
    # max(freq.values) = 3
    # if k in freq and freq[k] >= k and m <= k:
    #     return k
    # return -1

    # search([5, 5, 4, 4, 4]) == -1
    # freq =
