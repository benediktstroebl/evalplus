
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

    # ----------
    # Recursive solution
    # ----------
    # if list is empty, return 0
    # else
    #   sum of squares of numbers that are odd
    #     (those that are even are skipped)
    #
    #
    #     base case: if list is empty, return 0
    #
    # ----------
    # Iterative solution
    # ----------
    # sum of squares of numbers that are odd
    #    (those that are even are skipped)
    #   
    #     base case: if list is empty, return 0
    #    

    def rec_double_the_difference(lst):
        '''
        Recursive solution.
        '''
        # base case: if list is empty, return 0
        if lst == []:
            return 0
        # else
        else:
            # sum of squares of numbers that are odd
            #     (those that are even are skipped)
            sum_squares = 0
            if lst[0] %
