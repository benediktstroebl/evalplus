
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
    #get the even and odd values in the list
    evens = [i for i in lst if i % 2 == 0]
    odds = [i for i in lst if i % 2 == 1]
    
    #call the double_the_difference function again
    #this time, pass the odds list as an argument
    #the function will return the sum of the squares of all the odd values
    #in the odds list
    return double_the_difference(odds) + sum(evens)

