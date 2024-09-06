
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

    '''
    my solution:
    def double_the_difference(lst):
        return sum([x*x for x in lst if x%2!=0])
    '''
    #My solution
    #my_solution_2:
    def double_the_difference(lst):
        return sum([x*x for x in lst if x%2!=0 and x>0])

    #My solution - 1
    #my_solution_3:
    def double_the_difference(lst):
        return sum([x*x for x in lst if x%2!=0])+sum([y*y for y in lst if y%2==0])

    #My solution - 2
    #my_solution_4:
    def double_the_difference(lst):
        return sum([x*x for x in lst if x>0 and x%2!=0])
    #my_solution_5:
    def double_the_difference(lst):
        return sum([x*x for x in lst if x%
