
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
    
    #Solution 1
    # return sum([x**2 for x in lst if x % 2 == 1])
    
    #Solution 2
    # return sum([x**2 for x in lst if x % 2 != 0])
    
    #Solution 3
    # return sum([x**2 for x in lst if x in range(0,9999)])
    
    #Solution 4
    # return sum([x**2 for x in lst if x > -1 and x <= 9999])
    
    #Solution 5
    # return sum([x**2 for x in lst if x == 2 or x == 3 or x == 4 or x == 5 or x == 6 or x == 7 or x == 8 or x == 9])
    
    #Solution 6
    # return sum([x**2 for x in lst if x % 10 == 0])
    
    #Solution 7
    # return sum([x**2 for x in lst
