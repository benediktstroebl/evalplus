
def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
    
    If the input list is empty, return 0.
    '''
    #------------------------------
    # 1st solution:
    #------------------------------
    '''
    sum = 0
    for i in lst:
        if i < 0 or not isinstance(i, int):
            continue
        else:
            if (i % 2) != 0:
                sum += (i ** 2)
    return sum
    '''
    #------------------------------
    # 2nd solution:
    #------------------------------
    '''
    sum = 0
    for i in lst:
        if i < 0 or not isinstance(i, int):
            continue
        else:
            if (i % 2) != 0:
                sum += (i ** 2)
    return sum
    '''
    #------------------------------
    # 3rd solution:
    #------------------------------
    '''
    return sum((i**2 for i in lst if (i % 2) != 0))
    '''
    #------------------------------
    # 4th solution:
    #------------------------------
    '''
    return sum(i**2 for i in lst if (i % 2) != 0)
    '''
    #------------------------------
    # 5th solution:
    #------------------------------
    '''
    return sum(i**2 for i in lst if i % 2)
    '''
    #------------------------------
    # 6th solution:
    #------------------------------
    '''
    return sum(i**2 for i in lst if i%2 != 0)
    '''
    #------------------------------
    # 7th solution:
    #------------------------------
    '''
    return sum(i**2 for i in lst if not i%2)
    '''
    #------------------------------
    # 8th solution:
    #------------------------------
    '''
    return sum(i**2 for i in lst if i%2 == 0)
    '''
    #------------------------------
    # 9th solution:
    #------------------------------
    '''
    return sum(i**2 for i in lst if i%2 == 0)
    '''
    #------------------------------
    # 1
