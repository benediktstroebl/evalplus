
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
    if len(lst) == 0:
        return -1
    
    # Step 1: Initialise the output list 
    freq_list = []
    
    # Step 2: Loop through the list
    for num in lst:
        if num > 0:
            freq = lst.count(num)
            if freq >= num:
                freq_list.append((num, freq))
    
    # Step 3: Sort the list
    freq_list = sorted(freq_list, key = lambda x: (x[1], x[0]), reverse = True)
    
    # Step 4: Return the greatest value
    if freq_list[0][1] == 1:
        return -1
    else:
        return freq_list[0][0]
    
    # Alternative Solution
    # from collections import Counter
    # nums_freq = Counter(lst).items()
    # return max((f for n,f in nums_freq if n>0 and f>=n), default=-1)

